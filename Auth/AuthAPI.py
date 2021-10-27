from flask import Blueprint
from flask import request, jsonify, current_app
import sys
from db import db
from db import credentials
import jwt
sys.path.append("../")

auth_api = Blueprint("auth", __name__)

@auth_api.route('/register', methods=['POST'])
def register():
    username = request.args.get('username')
    pw = request.args.get('passwordHash')
    credentials.append({"username": username, "passwordHash": pw})
    return jsonify({'Status': 'Success', 'Message': 'Successfully registered'})

@auth_api.route('/login', methods=['POST'])
def login():
    try:
        token = request.args.get('token')
        if token != None:
            try:
                user_details = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms="HS256")
            except jwt.InvalidSignatureError:
                return jsonify({'Status':'Failed', 'Message': 'Invalid token'})
            if user_details in credentials:
                return jsonify({'Status':'Success', 'Message': 'Login Successful'})
            else:
                return jsonify({'Status':'Failed', 'Message': 'Wrong username or password'})

        username = request.form.get('username')
        pw = request.form.get('passwordHash')
        user = {
            "username": username,
            "passwordHash": pw
        }
        if user in credentials:
            new_token = jwt.encode(user, current_app.config['SECRET_KEY'], algorithm="HS256")
            return  jsonify({'Status': 'Success', 'token': new_token})
        else: 
            return jsonify({"Status": "Failed", 'Message': 'Wrong username or password'})
    except Exception as e:
           return jsonify({'Status': 'Failed', 'Message':str(e)}) 
