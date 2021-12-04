# Score API here
from flask import Blueprint, request, current_app, json, jsonify
import sys, jwt
from creds import *
from db import db
sys.path.append("../")

auth_api = Blueprint("auth", __name__)

credsArray = []
secretkey = current_app.config['SECRET_KEY']

@auth_api.route('/register', methods=["POST"])
def Register():
    newCred = request.get_json()
    # check if username is provided
    try:
        username = newCred["username"]
    except KeyError:
        return jsonify({"status": "fail", "message": "No username."})
  
    # check if password is provided
    try:
       passwordHash =  newCred["passwordHash"]
    except KeyError:
        return jsonify({"status": "fail", "message": "No password."})

    credsArray.append(newCred)

    return jsonify({"status": "success", "message": "Credentials successfully registered."}), 200


@auth_api.route('/login', methods=["POST"])
def Login():
    def checkCred(givenCred):
        # check if username is provided
        try:
            username = givenCred["username"]
        except KeyError:
            return jsonify({"status": "fail", "message": "No username."})

        # check if password is provided
        try:
            passwordHash = givenCred["passwordHash"]
        except KeyError:
            return jsonify({"status": "fail", "message": "No password."})
        for i in credsArray:
            if (username == i["username"] and passwordHash == i["passwordHash"]):
                token = jwt.encode({"userID": username, "passwordHash": passwordHash}, secretkey, algorithm="HS256")
                return jsonify({"status": "success", "token": token}), 200
            else:
                return jsonify({"status": "fail", "message": "Authentication failed."}), 401
    
    givenCred = request.get_json()
    token = request.arg.get("token")

   
    def checkToken():
       if (token != None):
         try:
            data = jwt.decode(token, secretkey, algorithm=["HS256"])
            return checkCred(data)
         except:
            data = givenCred
            try:
                return checkToken(data)
            except:
                return jsonify({"status": "fail", "message": "Bad token"})
        
        # no token provided in URL argument (fresh login)
       elif (token == None):
            return checkCred(givenCred)




