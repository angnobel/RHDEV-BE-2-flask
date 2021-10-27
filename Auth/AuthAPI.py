# Score API here
from flask import Blueprint
import sys

from flask.globals import current_app, request
from flask.json import jsonify
from db import db
import jwt
sys.path.append("../")

auth_api = Blueprint("auth", __name__)


myArray = []


@auth_api.route('/register', methods=["POST"])
def register():
    form = request.form
    username = form["username"]
    passwordHash = form["passwordHash"]
    myArray.append({
        "username": username,
        "passwordHash": passwordHash
    })
    token = jwt.encode(
        {
            "username": username,
            "passwordHash": passwordHash
        },
        current_app.config["SECRET_KEY"],
        algorithm="HS256"
    )

    return {
        "message": "success",
        "token": token
    }


@auth_api.route('/login', methods=["POST"])
def login():
    username = request.args.get("username")
    passwordHash = request.args.get("passwordHash")
    testUser = {
        "username": username,
        "passwordHash": passwordHash
    }
    if testUser in db:
        token = jwt.encode(
            testUser,
            current_app.config["SECRET_KEY"],
            algorithm="HS256"
        )
        return jsonify({
            "message": "success",
            "token": token
        })

    return jsonify({
        "message": "failed"
    })
