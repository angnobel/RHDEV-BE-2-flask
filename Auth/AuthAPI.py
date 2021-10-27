# Score API here
from flask import Blueprint, current_app, json, request
import sys
from db import db
import jwt

sys.path.append("../")

auth_api = Blueprint("auth", __name__)
usernames_hashedPasswords = {}

@auth_api.route("/register", methods=['POST'])
def store_username():
    req = request.form
    if "username" in req.keys() and "passwordHash" in req.keys():
        usernames_hashedPasswords[req["username"]] = req["passwordHash"]
        return {"status":"successful", "data": usernames_hashedPasswords}

@auth_api.route("/login", methods=['POST'])
def checkValidity():
    req = request.form
    if "username" in req.keys() and "passwordHash" in req.keys() and \
    req["username"] in usernames_hashedPasswords.keys() and \
    req["passwordHash"] in usernames_hashedPasswords[req["username"]]:
        token = jwt.encode({'userID': req["username"],
                            'passwordHash': req["passwordHash"]
                            }, "testing", algorithm="HS256")

        return {"status": "successful", "token": token}
    else:
        return { "status": "unsuccessful"}