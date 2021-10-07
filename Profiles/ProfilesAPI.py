# Profile API here
from flask import Blueprint
import sys
from db import db
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)

@profiles_api.route("/<int:userID>", methods = ["GET"])
def retrieve_profile(userID):
    profile = db[userID]
    name = profile["name"]
    scores = profile["scores"]

    string1 = "Hello " + str(name) + "!\n\n" + "Your scores are:\n"
    string2 = ""
    for (score in scores):
        string2 += str(score)
        if score != scores[-1]:
            string2 += ", "
    return string1 + string2