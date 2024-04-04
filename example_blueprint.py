import os
import json
from flask import Blueprint, jsonify, request
import pandas as pd
from grammar_enumeration import grammars

example_blueprint = Blueprint('example_blueprint', __name__)
# df = pd.read_json("grammar.json")
df = pd.DataFrame(grammars)
grammar_error_report_file_path = "/usr/local/grammar_error_report.json"
if not os.path.exists(grammar_error_report_file_path):
    with open(grammar_error_report_file_path, "w", encoding="utf-8") as fp:
        """create empty file"""


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
    data = request.get_json()
    with open(grammar_error_report_file_path, "a", encoding="utf-8") as fp:
        fp.write(json.dumps(data, ensure_ascii=False) + "\n")
    return jsonify({"data": data})
