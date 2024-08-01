import json
import logging
import os
import platform
import re
import sys
import time
import traceback
from collections import defaultdict

import pandas as pd
import redo
import requests
from tqdm import tqdm

LOG_FILE = "update_product_sku.log"
FLAG_FILE = "update_product_sku.flag"
post_pattern = re.compile(r"=[\d.]+[Cc][Mm]$")
pre_pattern = re.compile(r"^([\dGT]+) ")
special_pattern = re.compile(r"^(G00[2-6])")
pre_pattern_1 = re.compile(r"^([\dGT]{3,})-")


def setup_logger(name, log_file, level=logging.INFO):
    """Function to setup a logger with given name, log_file, and logging level."""

    # Create a custom logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create handlers
    console_handler = logging.StreamHandler()  # Handler for stdout
    file_handler = logging.FileHandler(
        log_file, encoding="utf-8"
    )  # Handler for log file
    formatter = logging.Formatter("[%(asctime)s] %(message)s")
    file_handler.setFormatter(formatter)

    # Set level for handlers
    console_handler.setLevel(level)
    file_handler.setLevel(level)

    # Create formatters and add them to handlers
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s %(message)s")
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


def trigger_xm_sync_stock(shop_id, item_id):
    cookies = {
        "Hm_lvt_a9dd154bf075440d56c848e86a69aee8": "1719130817,1719330836,1719723772,1720638209",
        "HMACCOUNT": "583152D75F8BEFB6",
        "XMSESSID": "0806bf6df12fc0087e899fff019ca897172123200811620610081",
        "Hm_lpvt_a9dd154bf075440d56c848e86a69aee8": "1721646427",
    }

    headers = {
        "Accept": "*/*",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json; charset=UTF-8",
        # 'Cookie': 'Hm_lvt_a9dd154bf075440d56c848e86a69aee8=1719130817,1719330836,1719723772,1720638209; HMACCOUNT=583152D75F8BEFB6; XMSESSID=0806bf6df12fc0087e899fff019ca897172123200811620610081; Hm_lpvt_a9dd154bf075440d56c848e86a69aee8=1721646427',
        "Origin": "https://xmhelper.com",
        "Pragma": "no-cache",
        "Referer": "https://xmhelper.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "xm-lang": "cn",
        "xm-version": "2.0",
    }

    json_data = {
        "data": {
            "shop_id": str(shop_id),
            "item_id": int(item_id),
        },
        "path": "taskshopee/sync/syncstock",
    }

    response = requests.post(
        "https://www.xmhelper.com/shopeeapi/taskshopee/sync/syncstock",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    return response.json()


def get_shoplist():
    cookies = {
        "Hm_lvt_a9dd154bf075440d56c848e86a69aee8": "1719130817,1719330836,1719723772,1720638209",
        "HMACCOUNT": "583152D75F8BEFB6",
        "XMSESSID": "0806bf6df12fc0087e899fff019ca897172123200811620610081",
        "country": "cn",
        "Hm_lpvt_a9dd154bf075440d56c848e86a69aee8": "1721616332",
    }

    headers = {
        "Accept": "*/*",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json; charset=UTF-8",
        "Origin": "https://xmhelper.com",
        "Pragma": "no-cache",
        "Referer": "https://xmhelper.com/selectshop",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "xm-lang": "cn",
        "xm-lazadadomain": "lazada.com.ph",
        "xm-shopeedomain": "shopee.ph",
        "xm-version": "2.0",
    }

    json_data = {}

    response = requests.post(
        "https://xmhelper.com/api/login/check",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    return response.json()["data"]["shops"]

shops = get_shoplist()
shop_id_to_my_name = {shop["shop_id"]: shop["my_name"] or shop["shop_name"] for shop in shops}

column_name_mapping = {
    "PSKU\n相同PSKU判断为同一款商品\nThe same PSKU is judged to be the same product": "PSKU",
    "商品名称\nProduct Name": "Product Name",
    "商品图片\nProduct Image": "Product Image",
    "CSKU": "CSKU",
    "CSKU名称\nCSKU Name": "CSKU Name",
    "CSKU图片\nCSKU Image": "CSKU Image",
    "规格名称 1\nVariation Name 1": "Variation Name 1",
    "规格名称 2\nVariation Name 2": "Variation Name 2",
    "规格属性 1\nVariation 1": "Variation 1",
    "规格属性 2\nVariation 2": "Variation 2",
    "库存\nStock": "Stock",
    "虚拟库存\nVirtual Stock": "Virtual Stock",
    "进货价\nPurchase Price": "Purchase Price",
    "包装重量KG\nPackage Weight": "Package Weight",
    "包装宽度CM\nPackage Width": "Package Width",
    "包装高度CM\nPackage Height": "Package Height",
    "包装长度CM\nPackage Length": "Package Length",
}


def update_product_sku(
    shop_id,
    product_id,
    shop_id_to_item_id_to_calculated_sku,
    item_id_to_detail,
    debug=True,
    log=print,
):
    cookies = {
        "XMSESSID": "7233c2452d14bebbffc8656257763c52171903910015420211221",
        "country": "ph",
        "Hm_lvt_a9dd154bf075440d56c848e86a69aee8": "1719039103",
        "Hm_lpvt_a9dd154bf075440d56c848e86a69aee8": "1719045362",
    }

    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json; charset=UTF-8",
        # 'Cookie': 'XMSESSID=7233c2452d14bebbffc8656257763c52171903910015420211221; country=ph; Hm_lvt_a9dd154bf075440d56c848e86a69aee8=1719039103; Hm_lpvt_a9dd154bf075440d56c848e86a69aee8=1719045362',
        "Origin": "https://xmhelper.com",
        "Referer": "https://xmhelper.com/app/stock/list",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "xm-lang": "cn",
        "xm-version": "2.0",
    }

    item_id_to_calculated_sku = shop_id_to_item_id_to_calculated_sku[shop_id]
    item = item_id_to_detail[product_id]
    variation_id_to_calculated_sku = item_id_to_calculated_sku[product_id]
    need_update = False
    for sku_detail in item["skus"]:
        variation_id = sku_detail["variation_id"]
        ori_variation_sku = sku_detail["variation_sku"]
        if variation_id in variation_id_to_calculated_sku:
            new_variation_sku = variation_id_to_calculated_sku[variation_id]
        else:
            new_variation_sku = ori_variation_sku
            if debug:
                log(f"Not Found sku for {sku_detail}")
        sku_detail["variation_sku"] = new_variation_sku

        if ori_variation_sku != new_variation_sku:
            need_update = True
            log(f"{product_id}: {ori_variation_sku} -> {new_variation_sku}")

    if not need_update:
        if debug:
            log(f"No Need Update Item {item['name']}")
        return None

    json_data = {
        "data": {"shop_id": shop_id, "item": item},
        "path": "shopeeproduct/update/sku",
    }

    response = requests.post(
        "https://xmhelper.com/shopeeapi/shopeeproduct/update/sku",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    log(response.content)
    return True


@redo.retriable(
    attempts=3,
    sleeptime=1,
    retry_exceptions=(
        requests.exceptions.ReadTimeout,
        requests.exceptions.ConnectionError,
    ),
)
def get_shopeeproduct_list(shop_id):
    cookies = {
        "Hm_lvt_a9dd154bf075440d56c848e86a69aee8": "1719130817,1719330836,1719723772,1720638209",
        "HMACCOUNT": "583152D75F8BEFB6",
        "XMSESSID": "0806bf6df12fc0087e899fff019ca897172123200811620610081",
        "Hm_lpvt_a9dd154bf075440d56c848e86a69aee8": "1721646427",
    }

    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json; charset=UTF-8",
        "Origin": "https://xmhelper.com",
        "Referer": "https://xmhelper.com/app/stock/list",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "xm-lang": "cn",
        "xm-version": "2.0",
    }

    json_data = {
        "data": {
            "shop_id": shop_id,
            "options": {
                "page": 1,
                "page_size": 80,
                "search": "",
                "status": "NORMAL",
                "item_sku": "",
                "variation_sku": "",
                "item_id": "",
                "variation_id": "",
            },
        },
        "path": "shopeeproduct/list",
    }

    response = requests.post(
        "https://xmhelper.com/shopeeapi/shopeeproduct/list",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    return response.json()


def extract_sku_detail(json_data, log=print):
    sku_details = []
    product_items = json_data["data"]["list"]
    for product in product_items:
        for sku_item in product["skus"]:
            sku_details.append(
                {
                    "item_id": product["item_id"],
                    "shop_id": product["shop_id"],
                    "item_sku": product["item_sku"],
                    "tier_variation": product["tier_variation"],
                    **sku_item,
                }
            )
    log(f"Got {len(product_items)} Product Item(s) {len(sku_details)} SKU(s)")
    return sku_details


def update_product_list(shop_id, log=print):
    json_data = get_shopeeproduct_list(shop_id)
    sku_details = extract_sku_detail(json_data, log=log)
    if sku_details:
        with open(f"sku_details_{shop_id}.json", "w", encoding="utf-8") as fp:
            fp.write(json.dumps(sku_details, ensure_ascii=False, indent=4))

    return sku_details


def generate_sku_variations(sku):
    variations = []
    parts = sku.split("-")
    prefix = "-".join(parts[:-1])
    sizes = parts[-1].split("/")
    for size in sizes:
        variations.append(f"{prefix}-{size}")
    variations.append(sku)
    variations.append(sku.replace("- ", "-"))
    variations.append(sku.replace(" -", "-"))
    return variations


def get_sku(detail, color_mapping, all_stand_sku_set):
    extra_mapping = {
        "Black Pink": "Pink Black",
    }

    item_sku_mapping = {
        "201-2": "201",
        "6688-2": "6688",
        "8008T-2": "8008T",
        "9004-2": "9004",
    }
    # print("=" * 12)
    # print(json.dumps(detail, indent=4, ensure_ascii=False))
    variation_id = detail["variation_id"]
    variation_id_to_tier_index = {
        str(variation["variation_id"]): variation["tier_index"]
        for variation in detail["tier_variation"]["variations"]
    }
    tier_variation = detail["tier_variation"]["tier_variation"]
    item_sku = detail["item_sku"]
    item_sku = item_sku_mapping.get(item_sku, item_sku)
    # if not item_sku:
    #     item_sku = tier_variation[0]["options"][0].split()[0].split("-")[0]
    tier_index = variation_id_to_tier_index[variation_id]

    parts = []
    need_add_item_sku = True
    for idx, item in enumerate(tier_variation):
        option = item["options"][tier_index[idx]]
        option = special_pattern.sub(r"\1 ", option)
        option = option.replace("  ", " ")
        option = option.replace("B8600", "8600")
        option = option.replace("B2202", "2202")
        option = option.replace("A8018", "8018")
        option = option.replace("536-1", "536")
        option = option.replace(item_sku, "").strip()
        if item["name"].casefold().startswith("siz"):
            option = option.replace("-", "/")
        if item["name"].casefold().startswith("colo") and pre_pattern_1.match(option):
            need_add_item_sku = False
            option = pre_pattern.sub(r"\1-", option)

        parts.append(option)


    if need_add_item_sku:
        parts = [item_sku] + parts

    if parts[-1] == "random":
        parts[-2], parts[-1] = parts[-1], parts[-2]

    parts = [part.strip() for part in parts if part.strip()]
    result_sku = "-".join(parts).replace("--", "-")
    result_sku = result_sku.replace("- ", "-")
    result_sku = result_sku.replace(" -", "-")
    result_sku = post_pattern.sub("", result_sku)
    result_sku = pre_pattern.sub(r"\1-", result_sku)
    parts = result_sku.split("-")
    parts[1] = parts[1].replace("+", " ")
    parts[1] = parts[1].replace("pin ", "pink ")
    parts[1] = parts[1].replace("/", " ")

    if parts[1] in color_mapping:
        parts[1] = color_mapping[parts[1]]
    if parts[1] in extra_mapping:
        parts[1] = extra_mapping[parts[1]]

    result_sku = "-".join(parts)
    result_sku = pre_pattern.sub(r"\1-", result_sku)
    result_sku = result_sku.replace("+", " ")
    result_sku = result_sku.replace("Khaki color", "Khaki")
    result_sku = result_sku.replace("Pinlk", "Pink")
    result_sku = result_sku.replace("blcak", "black")
    result_sku = result_sku.replace("Blcak", "Black")
    result_sku = result_sku.replace("0range", "Orange")
    result_sku = result_sku.replace("Grenn", "Green")
    result_sku = result_sku.replace("Gray", "Grey")
    result_sku = result_sku.replace("6688-Pink-", "6688-Pink White-")
    result_sku = result_sku.replace("9636-Khaki Green-", "9636-Khaki-")
    result_sku = result_sku.replace("-5L ", "-")
    result_sku = result_sku.replace("-5 ", "-")
    result_sku = result_sku.replace("9002-Grey-", "9002-Grey Black-")
    result_sku = result_sku.replace("9002-Green-", "9002-Green Black-")
    result_sku = result_sku.replace("9002-Black-", "9002-Black Black-")
    result_sku = result_sku.replace("7045-Khaki-", "7045-Khaki Green-")
    result_sku = result_sku.replace("Khkai", "Khaki")
    result_sku = result_sku.replace("43/45", "44/45")
    result_sku = result_sku.replace("9488 ", "9488-")
    result_sku = result_sku.replace("9488 ", "9488-")
    result_sku = result_sku.replace("7046-Grey-", "7046-Grey Black-")
    result_sku = result_sku.replace("7046-Green-", "7046-Green Khaki-")
    result_sku = result_sku.replace("7046-Khaki-", "7046-Khaki Black-")
    result_sku = result_sku.replace("7046-Black-", "7046-Black White-")
    result_sku = result_sku.replace("7046-White-", "7046-White Black-")
    result_sku = result_sku.replace("6007-Grey Black-", "6007-Grey-")
    result_sku = result_sku.replace("6007-Green Black-", "6007-Green-")
    result_sku = result_sku.replace("6007-Khaki Black-", "6007-Khaki-")
    result_sku = result_sku.replace("9003-Grey-", "9003-Grey Black-")
    result_sku = result_sku.replace("9003-White-", "9003-White Black-")
    result_sku = result_sku.replace("9003-Green-", "9003-Green Black-")
    result_sku = result_sku.replace("9003-Black-", "9003-Black Black-")
    result_sku = result_sku.replace("2202-Blue-", "2202-DGreen-")
    result_sku = result_sku.replace("2202-Green-", "2202-MDreen-")
    result_sku = result_sku.replace("6688-Khaki White-", "6688-White Khaki-")
    result_sku = result_sku.replace("9636-Brown Green-", "9636-Brown-")
    result_sku = result_sku.replace("2326-Purple White-", "2326-Prople White-")
    result_sku = result_sku.replace("2326-Purple-", "2326-Prople White-")
    result_sku = result_sku.replace("2203-Purple-", "2203-Prople-")
    result_sku = result_sku.replace("201-Khaki Green-", "201-Green Khaki-")
    result_sku = result_sku.replace("2326-Grey Black-", "2326-Black Grey-")
    result_sku = result_sku.replace("7046-Khaki Black-", "7046-Khaki Green-")
    result_sku = result_sku.replace("6007-Black-", "6007-Black Black-")
    result_sku = result_sku.replace("536-Green-", "536-Green White-")
    result_sku = result_sku.replace("9077-Grey Black-", "9077-Black Grey-")
    result_sku = result_sku.replace("2202-Mini Green-", "2202-MDreen-")
    result_sku = result_sku.replace("6611-Black Grey-", "6611-Grey Black-")
    result_sku = result_sku.replace("9634-Khaki Green-", "9634-Green-")
    result_sku = result_sku.replace("9002-9003-Black White-", "9003-Black White-")
    result_sku = result_sku.replace("2203-Green-", "2203-DGreen-")
    result_sku = result_sku.replace("536-Brownicon tick-", "536-Brown-")
    result_sku = result_sku.replace("6009-White Khaki-", "6009-Khaki White-")
    result_sku = result_sku.replace("  ", " ")
    result_sku = result_sku.replace("6688-Khaki White-", "6688-White Khaki-")
    result_sku = result_sku.replace("8010-Green Khaki-", "8010-Khaki-")
    result_sku = result_sku.replace("8010-Green White-", "8010-White-")
    result_sku = result_sku.replace("8010-Grey Black-", "8010-Black-")
    result_sku = result_sku.replace("8010-Grey Blue-", "8010-Blue-")
    result_sku = result_sku.replace("8010-Grey Brown-", "8010-Brown-")
    # result_sku = result_sku.replace("", "")

    if result_sku in {
        "8018-Black White",
        "8018-Blue Red",
        "8018-Green White",
        "8018-Khaki White",
    }:
        print(result_sku)
        print(detail)

    # print(variation_id)
    # print(item_sku)
    # print(f"SKU Rresult: {result_sku}")
    # df = df_mapping
    # res = df[(df.PSKU == item_sku) & (df["Variation 1"] == var_1) & (df["Variation 2"] == var_2)]
    # if res.shape[0] == 1:
    #     return res.loc[0, "CSKU"]
    # print("=" * 12)
    if len(result_sku.split("-")) > 3:
        parts = result_sku.split("-")
        result_sku = f"{parts[0]}-{parts[1]} {parts[2]}-{parts[3]}"

    parts = [part.strip() for part in result_sku.split("-")]
    try:
        parts[1] = color_mapping[parts[1]]
    except Exception:
        # print(f"not found color mapping: {parts[1]}。{result_sku}")
        # print(detail)
        pass
    result_sku = "-".join(parts)

    if result_sku.startswith("2008-"):
        parts = result_sku.split("-")
        parts[1] = "random"
        result_sku = "-".join(parts)
        return all_stand_sku_set.get(result_sku, result_sku)
    # return all_stand_sku_set[result_sku]

    result_sku = result_sku.replace("536-Brownicon tick-", "536-Brown-")
    result_sku = result_sku.replace("9488-Green Black-", "9488-Black Green-")
    # if result_sku == "2008-random-41":
    #     print(all_stand_sku_set.get(result_sku, "None"))
    return all_stand_sku_set.get(result_sku, result_sku)


def clear_log_file_content(log_file):
    with open(log_file, "w", encoding="utf-8"):
        pass


logger = setup_logger("XMHelper", LOG_FILE, logging.INFO)


def start_sync_sku():
    global logger
    with open(FLAG_FILE, "w", encoding="utf-8") as fp:
        fp.write("True")

    clear_log_file_content(LOG_FILE)
    print = logger.info
    current_folder = os.path.dirname(os.path.abspath(__file__))
    try:
        sku_file_path = os.path.join(current_folder, "all_sku.xlsx"
        )

        print(f"Using SKU file: {os.path.basename(sku_file_path)}")
        df_mapping = pd.read_excel(sku_file_path, dtype=str, skiprows=1).fillna("")
        df_mapping = df_mapping.rename(column_name_mapping, axis=1)

        all_sku_details = []

        print("*" * 32)
        for shop in shops:
            print(f"Fetching {shop['my_name'] or shop['shop_name']}({shop['shop_id']})")
            shop_id = shop["shop_id"]
            sku_details = update_product_list(shop_id, log=logger.info)
            all_sku_details.extend(sku_details)
        print("*" * 32)

        print(f"Total sku items: {len(all_sku_details)}")
        with open(f"sku_details_all.json", "w", encoding="utf-8") as fp:
            fp.write(json.dumps(all_sku_details, ensure_ascii=False, indent=4))

        unique_sku = [sku.strip() for sku in df_mapping.CSKU.unique()]

        print("Generating Unique SKU...")
        all_stand_sku_set = {}
        for sku in tqdm(unique_sku):
            variations = generate_sku_variations(sku)
            for variation in variations:
                all_stand_sku_set[variation] = sku

        color_mapping = {
            "Dgreen": "DGreen",
            "dgreen": "DGreen",
            "Purplo": "Purple",
            "purplo": "Purple",
        }
        colors = {sku.split("-")[1] for sku in all_stand_sku_set}

        print("Generating Color Mapping...")
        for color in tqdm(colors):
            color = color.strip()
            color_mapping[color] = color
            color_mapping[color.upper()] = color
            color_mapping[color.casefold()] = color
            parts = color.split()
            if len(parts) == 2:
                color_mapping[parts[0].capitalize() + " " + parts[1].casefold()] = color
                color_mapping[parts[0].casefold() + " " + parts[1].capitalize()] = color

        shop_id = "all"
        with open(f"sku_details_{shop_id}.json", "r", encoding="utf-8") as fp:
            all_sku_details = json.loads(fp.read())

        for detail in tqdm(all_sku_details):
            detail["calculated_sku"] = get_sku(detail, color_mapping, all_stand_sku_set)
            detail["my_name"] = shop_id_to_my_name[detail["shop_id"]]

        df_res = pd.DataFrame(all_sku_details)

        df_res.to_csv(os.path.join(current_folder, "all_sku_details.csv") , index=False)
        print(df_res.columns)
        print(df_res.shape)
        df_res["matched"] = df_res.calculated_sku.isin(all_stand_sku_set)
        no_matched = df_res[df_res.matched == False]
        print(no_matched.shape)
        no_matched.head()
        no_matched = no_matched.sort_values(
            by=["my_name", "item_sku", "calculated_sku"]
        )
        for index in no_matched.index:
            detail = no_matched.loc[index].to_dict()
            parts = detail["calculated_sku"].split("-")
            color = parts[1]
            if color not in color_mapping:
                no_matched.loc[index, "error_type"] = "颜色错误"
            elif len(parts) == 3:
                no_matched.loc[index, "error_type"] = "尺码错误"
            else:
                no_matched.loc[index, "error_type"] = "其他错误"

        no_matched[["stock", "my_name", "item_sku", "name", "calculated_sku", "error_type"]].to_csv(
           os.path.join(current_folder, "no_matched.csv") , index=False
        )


        shop_id_to_item_id_to_calculated_sku = defaultdict(dict)
        shop_id_to_item_id_to_calculated_sku = {
            shop["shop_id"]: defaultdict(dict) for shop in shops
        }
        for index in df_res.index:
            detail = df_res.loc[index].to_dict()
            if not detail["matched"]:
                continue

            shop_id_to_item_id_to_calculated_sku[detail["shop_id"]][detail["item_id"]][
                detail["variation_id"]
            ] = detail["calculated_sku"]

        for shop in shops:
            item_id_to_sync = None
            shop_id = shop["shop_id"]
            print(f"Updating Shop {shop_id} {shop['my_name'] or shop['shop_name']}...")
            json_data = get_shopeeproduct_list(shop_id)
            item_id_to_detail = {
                item["item_id"]: item for item in json_data["data"]["list"]
            }
            for item in tqdm(json_data["data"]["list"], file=sys.stdout):
                updated = update_product_sku(
                    shop_id,
                    product_id=item["item_id"],
                    shop_id_to_item_id_to_calculated_sku=shop_id_to_item_id_to_calculated_sku,
                    item_id_to_detail=item_id_to_detail,
                    debug=False,
                    log=lambda x: tqdm.write(str(x)),
                )
                if updated:
                    item_id_to_sync = item["item_id"]

            if item_id_to_sync:
                print(f"触发XM后台数据更新, {shop['my_name'] or shop['shop_name']}({shop_id}) 【同步中】")
                sync_result = trigger_xm_sync_stock(shop_id, item_id_to_sync)
                if sync_result["status"] == 200 and sync_result["message"] == "ok":
                    print(
                        f"触发XM后台数据更新, {shop['my_name'] or shop['shop_name']}({shop_id}) 【同步完成】"
                    )
                else:
                    print(
                        f"触发XM后台数据更新, {shop['my_name'] or shop['shop_name']}({shop_id}) 【同步失败】{sync_result}"
                    )

    except Exception:
        print(traceback.format_exc())
    print(f"SKU更新结束")
    with open(FLAG_FILE, "w", encoding="utf-8") as fp:
        fp.write("Finished")


if __name__ == "__main__":
    if platform.system().casefold() == "windows":
        start_sync_sku()
    else:
        while True:
            if not os.path.exists(FLAG_FILE):
                with open(FLAG_FILE, "w", encoding="utf-8") as fp:
                    pass

            with open(FLAG_FILE, "r", encoding="utf-8") as fp:
                run_flag = fp.read()

            if run_flag != "False":
                time.sleep(3)
                print("Sleeping...")
                continue

            start_sync_sku()
