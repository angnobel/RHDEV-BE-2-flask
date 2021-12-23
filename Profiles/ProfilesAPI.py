# Profile API here
from flask import Blueprint, app
import sys
from flask.json import jsonify
from flask.wrappers import Request
from db import db
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)

##############################################################
# GET /{id} to retrieve the name and all scores of a profile #
#            DELETE /{id} to delete a profile                #
##############################################################
@profiles_api.route("/<int:studentID>", methods=["GET", "DELETE"])
def retrieveStatus(studentID):
    if request.method == "GET":
        try:
            return db[studentID]
        except Exception:
            return jsonify({"message": "student ID does not exist"})

    elif request.method == "DELETE":
        try:
            db.remove(studentID)
            return jsonify({"message": "User Successfully deleted"})
        except Exception:
            return jsonify({"message": "User does not exist. Enter a valid student ID"})

    else:
        return jsonify({"message": "Invalid request"})
        

###########################################################
#    POST /profiles to create a new profile (name only)   #
###########################################################
@profiles_api.route("/profiles", methods=["POST"])
def newProfile(name):
    try:
        newSignUp = {"name": name}
        db.append(newSignUp)
        return jsonify({"message" : "Account created successfully"})

    except Exception:
        return jsonify({"message": "Error signing up"})
    
#######################################################################################
# GET /{id}/score?minScore= to retrieve all scores of a profile, above the min score. #
#                  If min score not provided, return all scores                       #
#######################################################################################
@profiles_api.route("/<int:studentID>/score?minScore=", methods=["GET"])
def minimum(studentID):
    try:
        results = db[studentID].get("scores")
        if "minScore" in request.args.keys():
            score = list(filter(lambda x: x > int(request.args["minScore"]), results))
            return jsonify({"results": score})

        else:
            return jsonify({"results": results})
    except Exception:
        return jsonify({"message": "Invalid request"})
