# Profile API here
from db import db
from flask import Blueprint, json, request, jsonify
import sys
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)


@profiles_api.route('/', methods=["POST"])
def addProfile():
    name = request.args.get("name")
    db.append({"name": name})

    return jsonify({
        "message": "success"
    })


@profiles_api.route('/<int:id>', methods=["GET", "DELETE"])
def getProfile(id):
    if request.method == "GET":
        returnData = db[id]
        return jsonify({
            "message": "success",
            "data": returnData
        })
    elif request.method == "DELETE":
        returnData = db[id]
        del db[id]
        return jsonify({
            "message": "success",
            "deleted": returnData
        })


@profiles_api.route('/<int:id>/score', methods=["GET"])
def getProfileMinScore(id):
    minScore = request.args.get("minScore")
    listOfScores = db[id].get("scores")
    for i in listOfScores:
        if i < minScore:
            del i
    return {
        "message": "success",
        "data": listOfScores
    }
