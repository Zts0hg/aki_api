import os
import time
from collections import defaultdict
from random import choice

import pandas as pd
from flask import Blueprint, Flask, jsonify, request

from tools import update_product_sku

japanese_word_blueprint = Blueprint("japanese_word_blueprint", __name__)


@japanese_word_blueprint.route("/quiz", methods=["GET"])
def quiz():
    records = [
        {
            "question": "ジュース",
            "options": [
                "【形容词/イ形容词】难懂，费解；难以做到",
                "【名词】果汁",
                "【副词】（数量）很多，相当多",
                "【名词】肚子，肠胃",
            ],
            "answer": "【名词】果汁",
        },
        {
            "question": "日",
            "options": [
                "【名词】日，太阳；阳光",
                "【形容词/イ形容词】难懂，费解；难以做到",
                "【副词】（数量）很多，相当多",
                "【名词】肚子，肠胃",
            ],
            "answer": "【名词】日，太阳；阳光",
        },
        {
            "question": "日",
            "options": ["ひ", "うつくしい", "くさ", "きのう"],
            "answer": "ひ",
        },
        {
            "question": "新聞社",
            "options": [
                "【形容词/イ形容词】难懂，费解；难以做到",
                "【副词】（数量）很多，相当多",
                "【名词】报社",
                "【名词】肚子，肠胃",
            ],
            "answer": "【名词】报社",
        },
        {
            "question": "新聞社",
            "options": ["うつくしい", "きのう", "くさ", "しんぶんしゃ"],
            "answer": "しんぶんしゃ",
        },
    ]
    return jsonify(choice(records))
