from Auth.AuthAPI import auth_api
from Profiles.ProfilesAPI import profiles_api
from flask import Flask
from db import db


# Write your flask code here

app = Flask(__name__)

app.register_blueprint(profiles_api, url_prefix="/profiles")
app.register_blueprint(auth_api, url_prefix="/auth")

@app.route('/', methods = ["GET"])
def main():
    return "Welcome User"

# In main: GET / homepage that returns a welcome message
# 
# In authentication API (/auth prefix) 
# POST /register stores a username and hashedPassword (given as hashed)
# 
# Store it in a local array Login /login checks if the provided information is valid and return a jwt token + success message

# Write your flask code here