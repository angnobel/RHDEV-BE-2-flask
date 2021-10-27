# Profile API here
from flask import Blueprint, request, jsonify
import sys
from db import db
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)

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
        return jsonify({"Status" : "Error", "Message" : "Don't have"})

    else:
        deleted = db[id]
        del db[id]

        return jsonify({"Status" : "Success", "New db" : db, "Deleted profile" : deleted})


@profiles_api.route('/<int:id>/score', methods = ["GET"])
def getabovemin(id):
    if id > len(db)-1:
        return jsonify({"Status" : "Error", "Message" : "No such ID"})

    min = request.args.get('minScore')
    s = db[id]["scores"]

    if min == '':
        return jsonify({"Status" : "Success", "Details" : s})
    
    score = list(filter(lambda s: s > int(min), s))#use assig
    

    return jsonify({"Status" : "Success", "Details" : score})

