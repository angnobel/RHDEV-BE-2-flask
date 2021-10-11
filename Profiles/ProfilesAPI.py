# Profile API here
from flask import Blueprint, jsonify
from flask import request
import sys
from db import db
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)

@profiles_api.route("/<int:id>", methods=['GET', 'DELETE'])
def get_details(id):
    try:
        if request.method == 'GET':
            return {"Status": "Success", "Data": db[id]}
        else:
            temp = db[id]
            del db[id]
            return jsonify({"Status": "Success", "Deleted": temp})
    except Exception as e:
        return jsonify({'Status': 'Failed', "Error": e})

@profiles_api.route("/profiles", methods=['POST'])
def add_details():
    try:
        name = request.args.get('name')
        db.append({"name": name})
        return jsonify({"Status": "Success", 'Added': db[-1]})
    except Exception as e:
        return jsonify({'Status': 'Failed', "Error": e})

@profiles_api.route("/<int:id>/score", methods=['GET'])
def get_min_score(id):
    try:
        min_score = request.args.get('minScore')
        display_details = db[id].copy()
        if min_score != None: 
            display_details["scores"] = list(filter(lambda score: score > int(min_score), display_details["scores"]))
        return jsonify({'Status': 'Success', 'Data': display_details['scores']})
    except Exception as e:
        return jsonify({'Status': 'Failed', "Error": e})

