from flask import Blueprint, request, jsonify
import json
import jwt
import sys
sys.path.append("../")

secret = "asldfjlkasdj"
#current_app.config['SECRET_KEY']

def db_read(): 
	return json.load(open("./users.json"))

def db_contains(obj):
	data = db_read()
	return obj in data

def db_findkey(username):
	data = db_read()
	for row in data:
		if (row["username"] == id):
			return row 
	return None

def db_insert(new_data): 
	data = db_read()
	if db_findkey(new_data["username"]):
			raise ValueError("Profile already exists") 
	data.append(new_data)
	json.dump(data, open("./users.json", "w"))

auth_api = Blueprint("auth", __name__)

@auth_api.route("/login", methods=["POST"])
def login():
	token = request.args.get("token")
	try:
		payload = jwt.decode(token, secret, 
				algorithms=["HS256"])
		if (db_contains(payload)):
			return jsonify({"error": None}), 200
	except Exception as e:
		print(str(e))

	obj = request.get_json(force=True)
	if db_contains(obj):
		token = jwt.encode(obj, secret,
				algorithm="HS256")
		return jsonify({"error": None, "token" : token}), 200
	return jsonify({"error": "incorrect user or password", "token": None}), 404 

@auth_api.route("/register", methods=["POST"])
def register():
	data = request.get_json(force=True)
	username = data["username"]
	passwordHash = data["passwordHash"]
	try:
		db_insert({"username": username, "passwordHash": passwordHash})
		return jsonify({"error": None}), 201
	except ValueError as e:
		return jsonify({"error": str(e)}), 403 
