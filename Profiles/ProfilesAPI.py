# Profile API here
from flask import Blueprint, request
import sys
from db import db
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)

@profiles_api.route("/", methods=["POST", "GET"])
def profiles():
    # POST: adds new profile
    if request.method == "POST":
        req = request.form
        if "name" in req.keys():
            # check if profile to create exists
            for i in db:
                if i["name"] == req["name"]:
                    return {"status": "error", "message": "profile already exists"}

            # adds new profile to db
            db.append({"name": req["name"], "scores": []})
            return {"status": "success", "new_profile": req["name"]}
        
        return {"status": "error"}

    # GET: returns all profiles
    if request.method == "GET":
        return {"status": "success", "data": db}

    
@profiles_api.route("/<string:id>", methods=["GET"])
def profiles_id(id):
    if request.method == "GET":
        # checks if id in the database
        print(id)
        for i in db:
            print(i["name"])
            if i["name"] == id:
                return {"status": "success", "data": i}
        
        return {"status": "error", "message": "profile not found"}