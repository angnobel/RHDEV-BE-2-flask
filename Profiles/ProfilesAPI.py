# Profile API here
from flask import Blueprint, json, request, jsonify
import sys
from db import db
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)

@profiles_api.route("/<int:id>", methods=["GET"])
def get_id(id):
    try:
        if id > len(db) -1 :
            return jsonify({"status": "error", "message" : "index out of range"})
        return jsonify({"data" : db[id], "status": "success"})
    except:
        return jsonify({"status": "error"})


@profiles_api.route("/create_profile", methods=["POST"])
def add_new_profile():
    try:
        data = request.form
        new_profile = { "name": data["name"], "scores" : []}
        db.append(new_profile)
        return jsonify({"added": new_profile, "status": "success"})
    except:
        return jsonify({"status": "error"})


@profiles_api.route("/<int:id>", methods=["DELETE"])
def delete_profile(id):
    
    if id > len(db) - 1:
        return jsonify({"status": "error", "message" : "index out of range"})

    del db[id]
    return jsonify({"deleted": db[id], "status": "success"})


@profiles_api.route("/<int:id>/score", methods=["GET"])
def get_scores_above_min(id):


    if id > len(db) - 1:
        return jsonify({"status": "error", "message" : "index out of range"})
    data = request.args
    scores = db[id]["scores"]
    
    if data.get("minScore") == None:
        return jsonify({"data" : scores, "status": "success" })
    else:
        scores_greater_than_min = list(filter(lambda x : x > int(data["minScore"]), scores))
        return jsonify({"data" : scores_greater_than_min, "status": "success" })
        

 

    




