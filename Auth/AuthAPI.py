# Score API here
from flask import Blueprint, current_app
import sys
import jwt

from flask.globals import request
from flask.json import jsonify
from db import *

sys.path.append("../")

auth_api = Blueprint("auth", __name__)

@auth_api.route("/register", methods=["POST"])
def register():

    try:
        if request.form.get("username") != None:
            data = request.form
        elif request.args.get("username") != None:
            data = request.args
    except:
        return jsonify({"message": "bad request", "status": "failure"})

    username = data["username"]
    password = data["passwordHash"]
    credentials.append({"username": username, "password": password})
    
    return jsonify({"message": "registered", "status": "success"})


@auth_api.route("/login", methods=["POST"])
def login():
    
    if request.args.get("token") != None:
        #check if valid user
        login_method = "token"
        token = request.args.get("token")
        try: 
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return jsonify({"status": "failure", "message": "Token Not Valid"})
        username = data["userID"]
        passwordHash = data["passwordHash"]
    else:
        login_method = "normal"
        if request.form.get("username") != None:
            data = request.form
        elif request.args.get("username") != None:
            data = request.args
        username = data["username"]
        passwordHash = data["passwordHash"]

    # checking if valid user
    valid = False
    for username_pw_dict in credentials:
        if username == username_pw_dict["username"] and passwordHash in username_pw_dict["password"]:
            valid = True
            break

    if not valid:
        if login_method == "token":
            return jsonify({"status": "failure", "message": "Token Not Valid"})
        else:
            return jsonify({"status": "failure", "message": "User not found"})
    
    if login_method == "token":
        return jsonify({"message": "logged in", "status": "success"})
    else:

        token = jwt.encode({'userID': username,
                            'passwordHash': passwordHash
                            }, current_app.config['SECRET_KEY'], algorithm="HS256")
        
        return jsonify({'token': token, "status": "success"})

    