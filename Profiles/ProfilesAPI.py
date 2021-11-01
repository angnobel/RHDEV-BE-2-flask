# Profile API here
from flask import Blueprint
import sys
from db import db
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)


@profiles_api.route('<string:name>', methods = ["GET"])
def get_one_profile(name):
    userInput = input()
    if userInput in db:
        return db[userInput]
    
    else:
        print("User does not exist")
