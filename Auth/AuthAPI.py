# Score API here
from flask import Blueprint
from flask import request
from flask import jwt
from flask import current_app
from flask import flash
import sys
from db import db
sys.path.append("../")

auth_api = Blueprint("auth", __name__)

temporaryLocalArr = []
@auth_api.route('/register', methods = ["POST"])
def register():
    if (request.args.get("username") == None or request.args.get("hashedPassword") == None):
        return "Error, Invalid body"
    temporaryLocalArr.append({
    "username": request.args.get("username"),
    "hashedPassword": request.args.get("hashedPassword")
    })
    return "successfully registered"

@auth_api.route('/login', methods = ["POST"])
def login():
    token = request.args.get("token")
    if token != None:
        data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
        if data in temporaryLocalArr:
            return "login successful"
        return "login unsuccessful"
    
    user = {
    "username": request.args.get("username"),
    "hashedPassword": request.args.get("hashedPassword")
    }
    if user in temporaryLocalArr:
        newToken = jwt.encode(user, current_app.config['SECRET_KEY'], algorithm="HS256")
        flash("login succesful")
        return { 
            "token" : newToken
        }
    
    return "login unsuccessful"

    


# In authentication API (/auth prefix) 
# POST /register stores a username and hashedPassword (given as hashed)
# 
# Store it in a local array Login /login checks if the provided information is valid and return a jwt token + success message