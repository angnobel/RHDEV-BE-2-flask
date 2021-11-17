import json
import jwt
from flask import Flask, Blueprint, request,jsonify
from db import datab
from db import profile_auth


auth_api = Blueprint('auth_api',__name__,url_prefix='/auth')


@auth_api.route('/register/<string:username>/<string:password>/', methods=['POST','GET'])
def register_user(username,password):
    passwordhash = hash(password)
    user_dict = {"username":username, "hashedPassword": passwordhash}
    if user_dict["hashedPassword"] == -9223363242168321331:
        return jsonify({"message":"failure", "status":"400"})
    else:
        profile_auth.append(user_dict)
        return jsonify({"message":"success", "status":"200"})



@auth_api.route('/login/<string:username>/<string:password>/', methods=['POST','GET'])
def user_login(username,password):
    passwordhash = hash(password)
    user_dict = {"username":username, "hashedPassword": passwordhash}
    match = list(filter(lambda a:a["username"] == username and a["hashedPassword"] ==passwordhash, profile_auth))
    try:
        if match[0] == user_dict:
            token = jwt.encode({"username":username, "hashedPassword": passwordhash}, "secret", algorithm="HS256")
            return jsonify({"token":token, "message":"success", "status":"200"})
    except:
            return jsonify({"message":"failure", "status":"401"})