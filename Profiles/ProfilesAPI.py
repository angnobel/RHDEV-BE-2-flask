# Profile API here
from flask import Blueprint, request
import sys
from db import db
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)

@profiles_api.route("/<int:userID>", methods = ["GET"])
def retrieve_profile(userID):
    profile = db[userID]
    name = profile["name"]

    if name == "@":
        return "Sorry, profile does not exist."

    scores = profile["scores"]

    string1 = "Hello " + str(name) + "!\n\n"
    string2 = "Your scores are:\n" + ""
    for score in scores:
        string2 += str(score)
        if score != scores[-1]:
            string2 += ", "
    return string1 + string2

@profiles_api.route("/profiles", methods = ["POST"])
def create_profile():
    content = request.get_json()
    content["scores"] = []
    db.append(content)
    name = content["name"]
    return "Successfully added " + name + " to database! :)"

@profiles_api.route("/<int:userID>", methods = ["DELETE"])
def delete_profile(userID):
    profile = db[userID]

    if profile["name"] == "@":
        return "Sorry, profile does not exist."
    
    name = profile["name"]
    profile["name"] = "@"
    return "Sorry " + name + ", you've been thanosSnapped"

@profiles_api.route("/<int:userID>/score", methods = ["GET"])
def get_min_score(userID):
    profile = db[userID]
    score_list = profile["scores"]
    
    if profile["name"] == "@":
        return "Sorry, profile does not exist."
    if len(profile["scores"]) == 0:
        return "You do not have any recorded results :("

    min_score = request.args.get('minScore')
    filtered_score_list = list(filter( lambda score:int(score) >= min_score , score_list))
    num_of_scores = len(filtered_score_list)
    if num_of_scores == 0:
        return "No scores found above " + str(min_score-1) + " :'("
    string2 = "There are a total of " + str(num_of_scores) + ". \nHere they are!: \n"
    for score in filtered_score_list:
        string2 += str(score)
        if score != filtered_score_list[-1]:
            string2 += ", "
    return string2