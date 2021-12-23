# Score API here
from flask import Blueprint
from flask.json import jsonify
import sys
from db import db, userInformation
sys.path.append("../")
import jwt
from datetime import _date, datetime

auth_api = Blueprint("auth", __name__)

########################################################################
# POST /register stores a username and hashedPassword (given as hashed)#
########################################################################

@auth_api.route("/register", methods=["POST"])
def register(username, passwordHash):
    try:
        newUser = {"username": username, "passwordHash": passwordHash, "createdAt": ""}
        userInformation.append(newUser)
        return jsonify({"message": "User created successfully"}), 200

    except Exception:
        return jsonify({"message": "Error in creating user"})

##############################################
#                LOGGING IN                  #
##############################################

@auth_api.route("/login", methods=["POST"])
def login(username, passwordHash):
    try:
        for i in userInformation:
            if datetime.today() < userInformation[i].get("createdAt") + datetime.timedelta(weeks=2):
                userInformation[i]["createdAt"] = datetime.today()
                token = jwt.encode({'username': username, 'passwordHash': passwordHash}, current_app.config['SECRET_KEY'], algorithm="HS256")
                return jsonify({'token': token, "message": "Logging in now"})
            
            # JWT Token Invalid but Username and Password still valid
            elif userInformation[i].get("username") == username:
                if userInformation[i].get("passwordHash") == passwordHash:
                    userInformation[i]["createdAt"] = datetime.datetime.now()
                    token = jwt.encode({'username': username, 'passwordHash': passwordHash}, current_app.config['SECRET_KEY'], algorithm="HS256")
                    return jsonify({'token': token, "message": "Logging in now"})

    except:
        return jsonify({"message": "Login error"})
