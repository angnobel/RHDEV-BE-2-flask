# Score API here
from flask import Blueprint, request, current_app, json
from Auth.Auth_db import Auth_db
import jwt
import sys
sys.path.append("../")

auth_api = Blueprint("auth", __name__)


@auth_api.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        req =  request.form

        # checks for valid body
        if "username" in req.keys() and "passwordHash" in req.keys():
            Auth_db.append({"username": req["username"], "passwordHash": req["passwordHash"]})
            return {"status": "success"}

        return {"status": "error", "message": "invalid body"}

@auth_api.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        req = request.form

        # checks for valid body
        if "username" in req.keys() and "passwordHash" in req.keys():
            username = req["username"]
            passwordHash = req["passwordHash"]

            token = jwt.encode({'username': username,'passwordHash': passwordHash}, current_app.config['SECRET_KEY'], algorithm='HS256')
            return json.jsonify({"status": "success", "token": token})
                
        return {"status": "error", "message": "invalid body"}



# For testing, returns Auth_db
# @auth_api.route("/", methods=["GET"])
# def auth():
#     if request.method == "GET":
#         return {"status": "success", "auth_db": Auth_db}