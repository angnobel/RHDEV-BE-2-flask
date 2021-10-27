from Auth.AuthAPI import auth_api
from Profiles.ProfilesAPI import profiles_api
from flask import Flask
from db import db
from db import *


# Write your flask code here

app = Flask(__name__)

app.config['SECRET_KEY'] = AUTH_SECRET_KEY
app.register_blueprint(profiles_api, url_prefix="/profiles")
app.register_blueprint(auth_api, url_prefix="/auth")

@app.route("/")
def hello_world():
    return "Welcome to the database!"

app.run