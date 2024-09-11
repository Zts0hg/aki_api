import json
import os
import time
from collections import defaultdict
from random import choice

import pandas as pd
from flask import Blueprint, Flask, jsonify, request

from tools import update_product_sku

japanese_quiz_blueprint = Blueprint("japanese_quiz_blueprint", __name__)

quiz_cache = {}


@japanese_quiz_blueprint.route("/selection/random", methods=["GET"])
def question_selection():
    questions = [
        {
            "question": "期末試験の結果（　　　　）、卒業できないこともある。",
            "options": ["からみると", "いかんでは", "に限って", "を機に"],
            "answer": "いかんでは",
            "explain": {
                "option_1": "名 + から見ると: 根据…… （后面常接「～かもしれない」「～こともある」等。）",
                "option_2": "名（の） + いかんでは: 唯独……、偏偏…… （后项往往是意想不到的事情）",
                "option_3": "名 + に限って: 从……来看 （可以直接接在表示人物的名词后面）",
                "option_4": "名 + を機に: 以……为契机、借……的机会",
            },
        },
        {
            "question": "彼のやったことは、教育者として（　　　　）ことだ。",
            "options": ["ありがちな", "欠かせない", "あるまじき", "言わずもがなの"],
            "answer": "あるまじき",
            "explain": {
                "option_1": "～がちな: 常常……、动不动就…… （表示常常发生不好的事情）",
                "option_2": "名 + に欠かせない: 在……方面不可或缺的",
                "option_3": "动词辞书形 + まじき + 名词: 作为……不该有的……",
                "option_4": "言わずもがなの + 名: 不应该说的……、不说为妙的……",
            },
        },
    ]
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
