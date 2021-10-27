# Score API here
from flask import Blueprint, request
import sys
import jwt
from db import db

sys.path.append("../")


auth_api = Blueprint("auth", __name__)



@auth_api.route("/register", methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.args.get('username')
        password = request.args.get('passwordHash')
        if(username == '') or (password == '') :
            return jsonify({'status':'error','message':'username or password field is empty'})
        else:
            details.append({"username": username, "passwordHash":password})
            return jsonify({"status":"success", "message":"user registered"})      

@auth_api.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.args.get('username')
        passwordHash = request.args.get('passwordHash')
        user_details = {'username':username,'passwordHash':passwordHash}
        #Upon successful login
        if user_details in details:
            token = jwt.econde({'username':username,'passwordHash':passwordHash},current_app.config['SECRET_KEY'],algorithm = 'HS256')
            return jsonify({'status':'success','token':token})
        else:
            return jsonify({'status':'error','message':'username or password entered incorrectly'})
