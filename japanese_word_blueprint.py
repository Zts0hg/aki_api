import json
import os
import time
from collections import defaultdict
from random import choice

import pandas as pd
from flask import Blueprint, Flask, jsonify, request

from tools import update_product_sku

japanese_word_blueprint = Blueprint("japanese_word_blueprint", __name__)

quiz_cache = {}


@japanese_word_blueprint.route("/quiz", methods=["GET"])
def quiz():
    global quiz_cache
    keyword = request.args.get("level")
    level_to_files = {
        0: ["kana_quiz.json"],
        1: ["N5_words.json", "N4_words.json"],
        2: ["N3_words.json", "N2_words.json"],
        3: ["N1_words.json"],
        4: ["words_10000.json"],
    }

    target_level = int(keyword)
    if target_level in quiz_cache:
        return jsonify(quiz_cache[target_level])

    files = level_to_files[target_level]
    words = []
    folder_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "japanese_words"
    )
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "r", encoding="utf-8") as fp:
            words += json.loads(fp.read())

    quiz_cache[target_level] = words
    return jsonify({"words": words})
