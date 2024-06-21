import hashlib
import json
import os
import platform
import re

import pandas as pd
from flask import Blueprint, jsonify, request, send_file

import text_to_audio
from assistant import Assistant
from grammar_enumeration import df_grammars

RE_WHITESPACES_PATTERN = re.compile(r"\s+")


def get_md5(content):
    content = content.encode("utf-8")
    md5_hash = hashlib.md5()
    md5_hash.update(content)
    return md5_hash.hexdigest()


question_pattern = re.compile(r"[（(](?:[\da-n]\s*[~\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF]+\s*)+[)）]")
example_blueprint = Blueprint('example_blueprint', __name__)
last_audio_content = [""]

# df = df_grammars
with open("grammars_N1-N5.json", "r", encoding="utf-8") as fp:
    df = pd.DataFrame(json.loads(fp.read()))
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
        df_res = df
        for item in keyword.split():
            df_res = df_res[df_res.content.str.replace(r"[（）()\s]", "", regex=True).str.contains(item)
                            | df_res.hiragana.str.replace(r"[（）()\s]", "", regex=True).str.contains(item)
                            | df_res.chinese_meaning.str.contains(item) | (df_res.source == item)]
        df_res["order"] = df_res.content.apply(len)
        df_res = df_res.sort_values(by="order")

    print(f"Search {df_res.shape[0]} records for keyword {keyword}")
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
    content_md5 = get_md5(RE_WHITESPACES_PATTERN.sub(" ", content))
    print(content)
    print(content_md5)
    audio_file_path = os.path.join(os.getcwd(), "japanese_grammar", "audio", f"{content_md5}.mp3")
    if os.path.exists(audio_file_path):
        return send_file(audio_file_path, mimetype=mimetype, as_attachment=False)

    if content != last_audio_content[0]:
        text_to_audio.generate_audio([("多语言模型", content)], audio_file, overwrite=True, xml_lang="ja-JP")
        last_audio_content[0] = content
        return send_file(audio_file, mimetype=mimetype, as_attachment=False)
    else:
        return send_file(audio_file, mimetype=mimetype, as_attachment=False)
