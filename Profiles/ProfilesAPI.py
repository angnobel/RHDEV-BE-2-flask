# Profile API here
from flask import Blueprint, request
import sys
from db import db
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)

@profiles_api.route("/<int:userID>", methods = ["GET"])
def retrieve_profile(userID):
    try:
         profile = db[userID]
    except IndexError:
        return {"status": "fail", "message": "profile not found"}
    
    name = profile["name"]
    if name == "@":
        return {"status": "fail", "message": "profile not found"}

    scores = profile["scores"]

    return {"status": "success",
    "message": {
        "name":name,
        "scores":scores
    }
    }

@profiles_api.route("/profiles", methods = ["POST"])
def create_profile():
    content = request.get_json()
    content["scores"] = []
    db.append(content)
    name = content["name"]
    return {"status": "success", "message": "profile added"}

@profiles_api.route("/<int:userID>", methods = ["DELETE"])
def delete_profile(userID):
    try:
         profile = db[userID]
    except IndexError:
        return {"status": "fail", "message": "profile not found"}
    
    if profile["name"] == "@":
        return {"status": "fail", "message": "profile not found"}
    
    name = profile["name"]
    profile["name"] = "@"
    return {"status": "success", "message": "profile deleted"}

@profiles_api.route("/<int:userID>/score", methods = ["GET"])
def get_min_score(userID):
    try:
         profile = db[userID]
    except IndexError:
        return {"status": "fail", "message": "profile not found"}
    
    score_list = profile["scores"]
    
    if profile["name"] == "@":
        return {"status": "fail", "message": "profile not found"}

    min_score = request.args.get('minScore')
    if min_score==None:
        min_score = 0
    else:
        min_score = int(min_score)
    
    filtered_score_list = list(filter( lambda score:int(score) >= min_score , score_list))
    num_of_scores = len(filtered_score_list)
    if num_of_scores == 0:
        return {"status": "success", "message": "no scores found"}

    return {"status": "success", "message": {"scores": filtered_score_list}}