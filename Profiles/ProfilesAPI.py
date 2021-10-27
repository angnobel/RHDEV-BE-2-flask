# Profile API here
from flask import Blueprint, request, jsonify
import sys
from db import db
sys.path.append("../")

profiles_api = Blueprint("profiles", name)

@profiles_api.route('/<int:id>/', methods = ["GET"])
def retrieve(id):
    if id > len(db)-1:
        return jsonify({"Status" : "Error", "Message" : "Don't have"})

    else:
        dets = db[id]
        return jsonify({"Status" : "Success", "Details" : dets})

@profiles_api.route('/', methods = ["POST"])#wont work on googlechrome only on postman,check on postman
def postid():
    newprofile = {}
    newprofname = request.form.get('name')
    newprofile["name"] = newprofname

    db.append(newprofile)

    return jsonify({"Status" : "Success", "Details" : newprofile})


@profiles_api.route('/<int:id>/', methods = ["DELETE"])
def deleteid(id):
    if id > len(db)-1:
        return jsonify({"Status" : "Error", "Message" : "No such ID"})

    else:
        deleted = db[id]
        del db[id]

        return jsonify({"Status" : "Success", "New db" : db, "Deleted profile" : deleted})


@profiles_api.route('/<int:id>/score', methods = ["GET"])
def getabovemin(id):
    if id > len(db)-1:
        return jsonify({"Status" : "Error", "Message" : "No such ID"})

    minscore = request.args.get('minScore')
    scores = db[id]["scores"]

    if minscore == '':
        return jsonify({"Status" : "Success", "Details" : scores})
    
    abovemin = list(filter(lambda score: score > int(minscore), scores))#use assig
    

    return jsonify({"Status" : "Success", "Details" : abovemin})

