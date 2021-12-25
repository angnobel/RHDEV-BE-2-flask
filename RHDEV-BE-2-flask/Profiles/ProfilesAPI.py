# Profile API here
from flask import Blueprint, app
import sys
from flask import json
from flask.json import jsonify
from db import db
sys.path.append("../")

print(type(db))
profiles_api = Blueprint("profiles", __name__)

###############################
#         Question 2          #
###############################
@profiles_api.route("/<int:studentID>", methods=["GET"])
def readProfile(studentID):
    try:
        return db[studentID]
    except Exception:
        return jsonify({"message": "student ID does not exist"})

###############################
#           Question 4        #
###############################
@profiles_api.route("/<int:studentID>", methods=["DELETE"])
def deleteProfile(studentID):
    try:
        db.pop(studentID)
        return jsonify({"message": "Successfully deleted"})

    except Exception:
        return jsonify({"message": "error 405 occured"})

###############################
#           Question 3        #
###############################
@profiles_api.route("/", methods=["POST"])
def newProfile(name):
    try:
        newSignUp = {"name": name}
        db.append(newSignUp)
        return jsonify({"message" : "Account created successfully"})

    except Exception:
        return jsonify({"message": "Error signing up"})




####################################################
#        Question 5 -- Do not know how to do       #
####################################################
#@profiles_api.route("/<int:studentID>/score?minScore=", methods=["GET"])
#def minimum(studentID):
 #   try:
  #      results = db[studentID].get("scores")
        #if "minScore" in request.args.keys():
   #         score = list(filter(lambda x: x > int(request.args["minScore"]), results))
    #        return jsonify({"results": score})

     #   else:
      #      return jsonify({"results": results})
    #except Exception:
     #   return jsonify({"message": "Invalid request"})
