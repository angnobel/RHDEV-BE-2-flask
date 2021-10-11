# Profile API here
from flask import Blueprint
import sys
from db import db
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)

@profiles_api.route("/<string:id>", methods = ["GET"])
def searchProfiles(id):
    for set in db:
        if id == set["name"]:
            return set
    return "Wrong id" #What type of error should I throw in here



# In profiles API (/profiles prefix) 
# GET /{id} to retrieve the name and all scores of a profile 
# POST /profiles to create a new profile (name only) 
# DELETE /{id} to delete a profile 
# GET /{id}/score?minScore= to retrieve all scores of a profile, above the min score 