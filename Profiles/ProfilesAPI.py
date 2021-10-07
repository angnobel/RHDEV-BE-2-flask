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