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
        return {"message": "fail", "data": "profile not found"}
    
    name = profile["name"]
    if name == "@":
        return {"message": "fail", "data": "profile not found"}

    scores = profile["scores"]

    return {"message": "success",
    "data": {
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
    return {"message": "success", "data": "profile added"}

@profiles_api.route("/<int:userID>", methods = ["DELETE"])
def delete_profile(userID):
    try:
         profile = db[userID]
    except IndexError:
        return {"message": "fail", "data": "profile not found"}
    
    if profile["name"] == "@":
        return {"message": "fail", "data": "profile not found"}
    
    name = profile["name"]
    profile["name"] = "@"
    return {"message": "success", "data": "profile deleted"}

@profiles_api.route("/<int:userID>/score", methods = ["GET"])
def get_min_score(userID):
    try:
         profile = db[userID]
    except IndexError:
        return {"message": "fail", "data": "profile not found"}
    
    score_list = profile["scores"]
    
    if profile["name"] == "@":
        return {"message": "fail", "data": "profile not found"}

    min_score = request.args.get('minScore')
    if min_score==None:
        min_score = 0
    else:
        min_score = int(min_score)
    
    filtered_score_list = list(filter( lambda score:int(score) >= min_score , score_list))
    num_of_scores = len(filtered_score_list)
    if num_of_scores == 0:
        return {"message": "success", "data": "no scores found"}

    return {"message": "success", "data": {"scores": filtered_score_list}}