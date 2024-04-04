import json
from flask import Blueprint, jsonify, request
import pandas as pd
from grammar_enumeration import grammars

example_blueprint = Blueprint('example_blueprint', __name__)
# df = pd.read_json("grammar.json")
df = pd.DataFrame(grammars)


@example_blueprint.route('/')
def index():
    keyword = request.args.get('keyword')

    if not keyword:
        return jsonify({
            "keyword": keyword,
            "data": [],
        })

    if keyword == "akiakiaki":
        df_res = df
    else:
        df_res = df[df.content.str.contains(keyword) | df.hiragana.str.contains(keyword) | df.meaning.str.contains(keyword)]
    return jsonify({
        "keyword": keyword,
        "data": [df.loc[index].to_dict() for index in df_res.index],
    })


@example_blueprint.route('/report_error', methods=["POST"])
def report_error():
    with open("/usr/local/grammar_error_report.json", "a", encoding="utf-8") as fp:
        fp.write(json.dumps(request.form, ensure_ascii=False))
    return jsonify({"form": request.form})
