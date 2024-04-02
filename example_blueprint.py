from flask import Blueprint, jsonify, request

example_blueprint = Blueprint('example_blueprint', __name__)


@example_blueprint.route('/')
def index():
    keyword = request.args.get('keyword')
    return jsonify({
        "keyword":
        keyword,
        "data": [{
            "content": "~うちに···",
            "hiragana": "",
            "meaning": "表示“在～的状态发生变化以前做···”。～表示发生变化以前的某种状态，···为表示有意志的动作的小句。",
            "usage": "dummy_usage",
            "example": [{
                "content": "dummy_example_sentence",
                "meaning": "dummy_example_meaning"
            }],
            "remark": "",
            "source": "",
        }, {
            "content": "~うちに···",
            "hiragana": "",
            "meaning": "表示“在～的状态发生变化以前做···”。～表示发生变化以前的某种状态，···为表示有意志的动作的小句。",
            "usage": "dummy_usage",
            "example": [{
                "content": "dummy_example_sentence",
                "meaning": "dummy_example_meaning"
            }],
            "remark": "",
            "source": "",
        }],
    })
