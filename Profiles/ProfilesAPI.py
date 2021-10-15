# Profile API here
from flask import Blueprint
from flask import request
from flask import flash
import sys
from db import db
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)

@profiles_api.route("/<string:id>", methods = ["GET"])
def searchProfiles(id):
    for set in db:
        if id == set["name"]:
            return set
    return "Wrong id" #What type of error should I throw in here

@profiles_api.route("/profiles", methods = ["POST"])
def createProfile():
    for set in db:
        if request.form["name"] == set["name"]:
            return "User already exist"

    db.append
    ({
        "name": request.form["name"],
        "score": [] #empty because it creates name only 
    })
    return "Profile created"

@profiles_api.route('/<string:id>', methods = ["DELETE"])
def deleteProfile(id):
    flash("Are you sure you want to delete profile?")
    flash("Please note that once deleted, lost data cannot be recovered. Are you sure?")
    # theres not much in the documentation for creating these messages. 
    for set in db:
        if id == set["name"]:
            db.remove(set)
            return "User has been deleted"
            
    return "User does not exist"

@profiles_api.route('/<string:id>/score', methods = ["GET"])
def profileScore(id):
    allScores = []
    for set in db:
        if id == set["name"]:
            allScores = set["scores"]
    if (allScores == []):
        return "No scores are found"    
    aboveMinScore = list(filter(lambda x: x > int(request.args.get("minScore"))), allScores)
    return aboveMinScore
# In profiles API (/profiles prefix) 
# GET /{id} to retrieve the name and all scores of a profile 
# POST /profiles to create a new profile (name only) 
# DELETE /{id} to delete a profile 
# GET /{id}/score?minScore= to retrieve all scores of a profile, above the min score 