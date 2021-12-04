# Profile API here
from flask import Blueprint, json, request, current_app
import sys
from db import db
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)



@profiles_api.route("/<string:id>", methods=['GET', "DELETE"])
def retrieve_delete_profiles(id):
    #Retrieve profiles
    if request.method=="GET":
        for profile in db:
            if profile["name"] == id:
                return {"status":"successful", "data": profile}
    #Delete profiles
    elif request.method=="DELETE":
        for profile in db:
            if profile["name"] == id:
                db.remove(profile) 
                return {"status":"successful", "data": db}

@profiles_api.route("/", methods=['POST', "GET"])
def create_new_profile(): 
    req = request.form
    if request.method=="POST":
        if "name" in req.keys():
            for profile in db:
                if profile["name"] == req["name"]:

                    return {"status":"unsuccessful", "message": "profile already exists"}
            
            db.append({"name": req["name"]})
            return {"status": "successful"}
    elif request.method=="GET":
        return {"status": "successful", "data": db}

@profiles_api.route("/<string:id>/score", methods=['GET'])
def get_above_min_scores(id):
    if "minScore" in request.args.keys():
        for profile in db:
            if profile["name"] == id:
                requested_scores = []
                if int(request.args["minScore"])==None:
                    requested_scores = profile["scores"]
                else:
                    for score in profile["scores"]:
                        if score>int(request.args["minScore"]):
                            requested_scores.append(score)
                
                return {"status":"successful", "data":requested_scores}

