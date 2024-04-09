import os
import json
from flask import Blueprint, jsonify, request, send_file
import pandas as pd
# from grammar_enumeration import grammars
import text_to_audio
import platform
from assistant import Assistant
import re

question_pattern = re.compile(r"[（(](?:[\da-n]\s*[~\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]+\s*)+[)）]")
example_blueprint = Blueprint('example_blueprint', __name__)
last_audio_content = [""]
# df = pd.DataFrame(grammars)
df = pd.read_json("grammar.json", dtype=str)
grammar_error_report_file_path = "/usr/local/grammar_error_report.json"

if platform.system().casefold() != "windows" and not os.path.exists(grammar_error_report_file_path):
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
        df_res = df[df.content.str.contains(keyword) | df.hiragana.str.contains(keyword) | df.chinese_meaning.str.contains(keyword) | (df.source == keyword)]
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


@example_blueprint.route('/analyze', methods=["POST"])
def analyze_sentence():
    data = request.get_json()
    content = data["content"]
    content = re.sub("\s+", " ", content)
    if question_pattern.search(content):
        process_method = Assistant.answer_question
    else:
        process_method = Assistant.analyze_sentence

    result = process_method(content=content)
    print("=" * 32)
    print(content)
    print(process_method.__name__)
    print(result)
    print("=" * 32)

    return jsonify({"data": result})


@example_blueprint.route('/speak')
def stream_audio():
    audio_file = 'audio.mp3'  # Replace with your audio file path
    mimetype = 'audio/mp3'  # Modify based on your audio file format
    content = request.args.get('content')
    print(content)
    if content != last_audio_content[0]:
        text_to_audio.generate_audio([("多语言模型", content)], audio_file, overwrite=True, xml_lang="ja-JP")
        last_audio_content[0] = content
        return send_file(audio_file, mimetype=mimetype, as_attachment=False)
    else:
        return send_file(audio_file, mimetype=mimetype, as_attachment=False)
