from Auth.AuthAPI import auth_api
from Profiles.ProfilesAPI import profiles_api
from flask import Flask
from db import db


# Write your flask code here

app = Flask(__name__)
app.config['SECRET_KEY'] = AUTH_SECRET_KEY
app.register_blueprint(profiles_api, url_prefix="/profiles")
app.register_blueprint(auth_api, url_prefix="/auth")

@app.route("/", methods = ["GET"])
def hello():
    return "halo"
if __name__== "main":
    app.run("localhost", port=8080)