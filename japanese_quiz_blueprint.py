import json
import os
from random import choice

from flask import Blueprint, jsonify

japanese_quiz_blueprint = Blueprint("japanese_quiz_blueprint", __name__)
current_folder = os.path.dirname(os.path.abspath(__file__))

quiz_cache = {}


@japanese_quiz_blueprint.route("/selection/random", methods=["GET"])
def question_selection():
    if quiz_cache.get("selection_questions"):
        return jsonify(choice(quiz_cache["selection_questions"]))

    with open(
        os.path.join(current_folder, "japanese_quiz", "all_select_questions.json"),
        "r",
        encoding="utf-8",
    ) as fp:
        questions = [json.loads(line) for line in fp.readlines()]

    quiz_cache["selection_questions"] = questions
    return jsonify(choice(questions))


@japanese_quiz_blueprint.route("/sort/random", methods=["GET"])
def question_sort():
    questions = [
        {
            "question": "9月も半ばで、やっと ________ ________ ________ ________ 。",
            "options": [
                "1 涼しくなった",
                "2 ぶり返した",
                "3 また残暑が",
                "4 と思いきゃ",
            ],
            "answer": "1432",
            "explain": {
                "translation": "【译文】九月都过了一半了,原以为终于要凉快了,没想到又热了起来。",
                "analysis": "【解析】选项3「また残暑が」与选项2「ぶり返した」构成主谓短语。选项1置于选项4之前,构成「と思いきゃ」的句型,表示“原以为……（却……）。”",
            },
        },
        {
            "question": "面接のとき、 ________ ________ ________ ________ 困る。",
            "options": ["1 ようでは", "2 話もできない", "3 緊張の", "4 あまり"],
            "answer": "3421",
            "explain": {
                "translation": "【译文】面试时,如果由于过于紧张而说不出话来的话就不好办了。",
                "analysis": "【解析】选项1「〜ようでは」表示“如果……的话”,后项常用「困る/だめだ」等负面的表达方式,因此选项1置于最后一个空。选项4「動辞書形/名一の+あまり」表示由于程度过甚,导致了某种结果,因此选项3置于选项4之前。选项2「話もできない」表示“紧张的结果”,置于选项4之后。",
            },
        },
    ]
    return jsonify(choice(questions))


@japanese_quiz_blueprint.route("/instant/random", methods=["GET"])
def question_instant_response():
    return jsonify({})
