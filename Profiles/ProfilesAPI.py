# Profile API here
from flask import Blueprint, request, json, jsonify
import sys
from db import db
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)

@profiles_api.route("/", methods=['GET'])
def welcome():
    return 'Welcome to Profiles'

@profiles_api.route("/profiles", methods = ['POST'])
#This function creates a new profile based on the name passed in
def create_profile():
    if request.method == 'POST':
        req = request.form
        if "name" in req.keys():
        #check for whether profile already exists
            for i in db:
                if i["name"] == req["name"]:
                    return jsonify({"status":"error", "message":"profile already exists"})
        

        db.append({"name" : req["name"], "scores":[]})
        return jsonify({"status":"success","message":"profile created"})

    return jsonify({"status":"error"})


@profiles_api.route("/<int:id>", methods = ['GET'])
def retrieve_all_details(id):
    if request.method == "GET":
        #check whether profile exists
        if id > len(db) - 1:
            return jsonify({"status":"error","message":"profile doesn't exist"})
            
        else:
            i = db[id]
            return jsonify({"status":"success","data": i})
        

@profiles_api.route("/<int:id>", methods = ["DELETE"])
def delete_profile(id):
    if request.method == 'DELETE':
        if id > len(db) - 1:
            return jsonify({"status":"error","message":"profile doesn't exist"})
        
        else:
            db.remove(id)
            return jsonify({"status":"success", "message":"profile deleted"})
    
    

@profiles_api.route("/<int:id>/score", methods=['GET'])
def retrieve_min_score(id):
    if request.method == 'GET':
        if id > len(db) - 1:
            return jsonify({"status":"error","message":"profile doesn't exist"})
        else:
            result = db[id]["scores"]
            if "minScore" in request.args.keys():
                score = list(filter(lambda x: x > int(request.args["minScore"]), result))
                return jsonify({"status":"success", "scores": score})
            else:

                return jsonify({"status":"success", "scores": result})
    return jsonify({"status":"error"})
        