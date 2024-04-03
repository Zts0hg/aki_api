from flask import Blueprint, jsonify, request

example_blueprint = Blueprint('example_blueprint', __name__)


@example_blueprint.route('/')
def index():
    keyword = request.args.get('keyword')
    return jsonify({
        "keyword":
        keyword,
        "data": [{
            "content":
            "~ 際 (に)",
            "hiragana":
            "~ さい(に)",
            "meaning":
            "~とき 硬い言い方（…………时候。书面语。）",
            "usage":
            "名の・動 辞書形/た形 +際(に)",
            "example": [{
                "content": "① この整理券は、 商品受け取りの際、必要です。",
                "hiragana": "このせいりけんは、 しょうひんうけとりのさい、ひつようです。",
                "meaning": "这张排号单在领取商品时需要用到。"
            }, {
                "content": "②こちらの会議室をご利用になる際は、 受付で必要事項をご記入ください。",
                "hiragana": "こちらのかいぎしつをごりようになるさいは、 うけつけでひつようじこうをごきにゅうください。",
                "meaning": "使用这间会议室时,请在前台登记必要事项。"
            }, {
                "content": "③アメリカの大統領は来日した際に、 わたしたちの大学でスピーチを行った。",
                "hiragana": "アメリカのだいとうりょうはらいにちしたさいに、 わたしたちの大学でスピーチを行った。",
                "meaning": "美国总统访问日本时,在我们大学做了演讲。"
            }],
            "remark":
            "主要接在表达行为、事件等的动词 (「使う・完成する」等) 和名詞 (「搭乗・外出」 等)后。多用于公共场合等,不太用于日常的普通事情。",
            "source":
            ""
        }],
    })
