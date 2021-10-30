# Score API here
from flask import Blueprint, request, current_app, json
import sys, jwt
from db import *
sys.path.append("../")

auth_api = Blueprint("auth", __name__)

@auth_api.route("/register", methods = ["POST"])
def register():
    content = request.get_json()
    try:
        # Check if username is provided
        userName = content["userName"]
    except KeyError:
        return {"status": "fail", "message": "no userName"}
    try:
        # Check if password is provided
        passwordHash = content["passwordHash"]
    except KeyError:
        return {"status": "fail", "message": "no password"}
    
    credentials[userName] = (
        {
            "userName": userName,
            "passwordHash": passwordHash
        }
    )
    return {"status": "success", "message": "registered successfully"}

@auth_api.route("/login", methods = ["POST"])
def login():
    content = request.get_json()
    try:
        # Check if username is provided
        userName = content["userName"]
    except KeyError:
        return {"status": "fail", "message": "no userName"}
    try:
        # Check if password is provided
        passwordHash = content["passwordHash"]
    except KeyError:
        return {"status": "fail", "message": "no password"}
    
    try:
        #Check for username and password in credentials dictionary
        exists = credentials[userName]["passwordHash"] == passwordHash
    except KeyError:
        return {"status": "fail", "message": "username or password is wrong"}
    if exists:
        token = jwt.encode({"userName": userName,"passwordHash": passwordHash}, 
            current_app.config["AUTH_SECRET_KEY"], algorithm="HS256")
        return json.jsonify({"status": "success", 
        "token": token})
    else:
        return {"status": "fail", "message": "username is wrong"}



