from flask import Blueprint, request, jsonify
import json
import sys
sys.path.append("../")

def db_read(): 
	return json.load(open("./profiles.json"))

def db_findkey(name):
	data = db_read()
	for row in data:
		if (row["name"] == name):
			return row 
	return None

def db_insert(new_data): 
	data = db_read()
	if db_findkey(new_data["name"]):
			raise ValueError("Profile already exists") 
	data.append(new_data)
	json.dump(data, open("./profiles.json", "w"))

def db_delete(name):
	data = db_read()
	row = db_findkey(name)
	if row:
		data.remove(row)
		json.dump(data, open("./profiles.json", "w"))
	else: 
		raise ValueError("Profile not found") 
		

profiles_api = Blueprint("profiles", __name__)

# gets data of matching profile 
@profiles_api.route("/<name>", methods=["GET"])
def read(name):
	row = db_findkey(name)
	if row:
		return jsonify({"error": None, "data" : row}), 200
	else: 
		return jsonify({"error": "not found", "data": None}), 404 

# creates new profile
@profiles_api.route("/<name>", methods=["POST"])
def create(name):
	try:
		db_insert({"name": name, "scores":[]})
		return jsonify({"error": None}), 201
	except ValueError as e:
		return jsonify({"error": str(e)}), 403 

# deletes matching profile
@profiles_api.route("/<name>", methods=["DELETE"])
def delete(name):
	try: 
		db_delete(name)
		return jsonify({"error": None}), 201
	except ValueError as e:
		return jsonify({"error": str(e)}), 403 

# gets scores of matching profile, optionally filtered > minScore
@profiles_api.route("/<name>/score", methods=["GET"])
def read_minscore(name):
	minScore = int(request.args.get("minScore") or 0)
	row = db_findkey(name)
	if row:
		return jsonify({"error": None, "data" : list(filter(lambda x:x > minScore, row["scores"]))}), 200
	else: 
		return jsonify({"error": "not found", "data": None}), 404 
