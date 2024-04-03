from flask import Blueprint, jsonify, request
import pandas as pd

example_blueprint = Blueprint('example_blueprint', __name__)
df = pd.read_json("grammar.json")


@example_blueprint.route('/')
def index():
    keyword = request.args.get('keyword')
    df_res = df[df.content.str.contains(keyword) | df.hiragana.str.contains(keyword) | df.meaning.str.contains(keyword)]

    return jsonify({
        "keyword": keyword,
        "data": [df.loc[index].to_dict() for index in df_res.index],
    })
