import os
import time
from collections import defaultdict

import pandas as pd
from flask import Blueprint, Flask, jsonify, request

from tools import update_product_sku

tool_blueprint = Blueprint("tool_blueprint", __name__)


def lock_and_sync():
    global task_running
    update_product_sku.start_sync_sku()
    task_running = False


task_running = False
start_time = time.perf_counter() - 600


@tool_blueprint.route("/upload_sku", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file part", 400

    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    if file:
        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "tools", "all_sku.xlsx"
        )
        file.save(file_path)
        return "File uploaded successfully", 200


@tool_blueprint.route("/sync_sku", methods=["GET"])
def sync_sku():
    global start_time
    global task

    if not os.path.exists(update_product_sku.LOG_FILE):
        with open(update_product_sku.LOG_FILE, "w", encoding="utf-8"):
            pass

    if not os.path.exists(update_product_sku.FLAG_FILE):
        with open(update_product_sku.FLAG_FILE, "w", encoding="utf-8"):
            pass

    with open(update_product_sku.FLAG_FILE, "r", encoding="utf-8") as f:
        run_flag = f.read().strip()

    if run_flag == "Finished":
        with open(update_product_sku.FLAG_FILE, "w", encoding="utf-8") as fp:
            fp.write("")
        with open(update_product_sku.LOG_FILE, "r", encoding="utf-8") as log:
            log_content = log.read()

        df = pd.read_csv("tools/no_matched.csv", dtype=str).fillna("")
        no_matched = defaultdict(list)
        target_fields = (
            "stock",
            "item_sku",
            "name",
            "calculated_sku",
            "error_type",
        )
        for index in df.index:
            detail = df.loc[index].to_dict()
            no_matched[detail["my_name"]].append(
                tuple(str(detail[field]) for field in target_fields)
            )

        return jsonify(
            {"running": False, "message": log_content, "no_matched": dict(no_matched)}
        )

    if run_flag == "True" and time.perf_counter() - start_time < 600:
        with open(update_product_sku.LOG_FILE, "r", encoding="utf-8") as log:
            log_content = log.read()
        return jsonify({"running": True, "message": log_content})

    start_time = time.perf_counter()
    with open(update_product_sku.FLAG_FILE, "w", encoding="utf-8") as fp:
        fp.write("False")
    return jsonify({"running": False, "message": "start running"})
