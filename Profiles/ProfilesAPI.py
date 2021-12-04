# Profile API here
from flask import Blueprint, json, request, jsonify
import sys
from db import db
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)

@profiles_api.route('/<int:id>', methods=["GET"])
def getProfile(id):
    try:
        profile = db[id]
    except IndexError:
        return jsonify({"status": "fail", "message": "Profile not found."})

    return jsonify({"status": "success", "profile": profile}), 200


@profiles_api.route('/', methods=["POST"])
def addProfile():
    newProfile = request.get_json()
    newProfile["scores"] = []
    db.append(newProfile)
    return jsonify({"status": "success", "message": "New profile added."}), 200


@profiles_api.route('/<int:id>', methods=["DELETE"])
def deleteProfile():
    try:
        profile = db[id]
    except IndexError:
        return jsonify({"status": "fail", "message": "Profile not found."})
    
    db.pop(id)
    return jsonify({"message": "success", "message": "Profile deleted."}), 200

@profiles_api.route('/<int:id>/score', methods=["GET"])
def getMinScore():
    try:
        profile = db[id]
    except IndexError:
        return jsonify({"status": "fail", "message": "Profile not found."})

    minScore = request.args.get("minScore")
    ScoreList = profile.get("scores")
    if minScore == None:
        minScore == 0
    else:
         minScore == int(minScore)

    def aboveMinScore(i):
        if i >= minScore:
            return i
    
    ScoresAboveMin = list(filter(aboveMinScore, ScoreList))

    return jsonify({"status": "success", "scores": ScoresAboveMin}), 200
            

