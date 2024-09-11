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
        os.path.join(current_folder, "japanese_quiz", "all_selection_questions.json"),
        "r",
        encoding="utf-8",
    ) as fp:
        questions = [json.loads(line) for line in fp.readlines()]

    quiz_cache["selection_questions"] = questions
    return jsonify(choice(questions))


@japanese_quiz_blueprint.route("/sort/random", methods=["GET"])
def question_sort():
    if quiz_cache.get("sort_questions"):
        return jsonify(choice(quiz_cache["sort_questions"]))

    with open(
        os.path.join(current_folder, "japanese_quiz", "all_sort_questions.json"),
        "r",
        encoding="utf-8",
    ) as fp:
        questions = [json.loads(line) for line in fp.readlines()]

    quiz_cache["sort_questions"] = questions
    return jsonify(choice(questions))


@japanese_quiz_blueprint.route("/instant/random", methods=["GET"])
def question_instant_response():
    return jsonify({})
