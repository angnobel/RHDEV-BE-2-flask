# Score API here
from flask import Blueprint, request, current_app, json, jsonify
import sys
from db import db
import pyjwt
sys.path.append("../")

auth_api = Blueprint("auth", __name__)

credsArray = []
username = request.arg.get("username")
passwordHash = request.arg.get("passwordHash")
token = jwt.encode({'userID': username, 'passwordHash': passwordHash}, current_app.config['SECRET_KEY'], algorithm="HS256")

@auth_api.route('/register', methods=["POST"])
def storeCredentials():
    credsArray.append({"username": username, "passwordHash": passwordHash})
    return jsonify({"message": "SUCCESS", "data": {"username": username, "hashedPassword": hashedPassword}}), 200 


@auth_api.route('/login', methods=["GET"])
def loginSuccess():
    testUser = {"username": username, "passwordHash": passwordHash}
    if (testUser in credsArray):
            token
            return jsonify({"message": "success", "token": token}), 200
    
    elif (not(testUser in credsArray)):
            return jsonify({"message": "failed"}), 401

    

try: 
    username
    passwordHash
except ValueError:
    print("No username or password input.")
except:
    print("An error occurred.")

@auth_api.route('/login', methods=["GET"])
def authToken():
    testtoken = request.arg.get("token")
    data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
    if (testtoken == "sdlkaskdnalsdnsald"):
        if (data in credsArray):
            return jsonify({"message": "success"}), 200
        elif (not(data in credsArray)):
            return jsonify({"message": "failed"}), 401

    elif (not(testtoken == "sdlkaskdnalsdnsald")):
            return jsonify({"message": "failed"}), 401
    
    currentUser = credsArray.User.find_one({'userID': data['userID'], 'passwordHash': data['passwordHash']})
    
jsonify({'token': token}), 200




