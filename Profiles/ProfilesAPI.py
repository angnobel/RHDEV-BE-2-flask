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
        
    return jsonify({"status": "success", "data": profile})


@profiles_api.route('/profiles', methods=["POST"])
def addProfile():
    newProfile = request.get_json()
    newProfile["scores"] = []
    db.append(newProfile)
    return jsonify({"status": "success", "message": "New profile added."})


@profiles_api.route('/<int:id>', methods=["DELETE"])
def deleteProfile():
    NameScore = db[id]
    del NameScore
    return jsonify({"message": "SUCCESS", "data": NameScore}), 200

@profiles_api.route('/<int:id>/score?minScore=', methods=["GET"])
def getMinScore():
    minScore = request.args.get("minScore")
    ScoreList = db[id].get("scores")
    def aboveMinScore(i):
        if i >= minScore:
            return i
    
    ScoresAboveMin = list(filter(aboveMinScore, ScoreList))

    return jsonify({"message": "SUCCESS", "data": ScoresAboveMin}), 200
            

