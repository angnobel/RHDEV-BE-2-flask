# Score API here
from flask import Blueprint, request, jsonify, current_app
import sys
from db import db, cred
import jwt
sys.path.append("../")

auth_api = Blueprint("auth", __name__)
@auth_api.route('/register', methods = ["POST"])
def reg():
    
    def regdet(argsform):
        username = argsform.get('username')
        hashedPassword = argsform.get('passwordHash')

        if (username == '') or (hashedPassword == ''):
            return jsonify({"Status" : "Failed", "Message" : "Username or Password not available"})
        else:
            cred.append({"username" : username, "passwordHash" : hashedPassword})
            return jsonify({"Status" : "Success", "Message" : "Registered"})

    if request.args.get('username'):
        return regdet(request.args)

    elif request.form.get('username'):
        return regdet(request.form)
    
@auth_api.route('/login', methods = ["POST"])
def login():

    def logindetails():
        username = request.form.get('username')
        hashedPassword = request.form.get('passwordHash')
        return username, hashedPassword

    det = logindetails()
    username = det[0]
    hashedPassword = det[1]

    checkuser = {"username":username, "passwordHash":hashedPassword}
    if checkuser in cred: 
        token = jwt.encode({'userID': username,
                            'passwordHash': hashedPassword
                            }, current_app.config['SECRET_KEY'], algorithm="HS256")

        return jsonify({'Status': 'Success', 'token': token})

    return jsonify({'Status': 'Failed', 'Message': 'Username or Password does not match'})