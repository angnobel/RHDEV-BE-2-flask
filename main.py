from Auth.AuthAPI import auth_api
from Profiles.ProfilesAPI import profiles_api
from flask import Flask
from db import db


app = Flask(__name__)

@app.route("/", methods = ["GET"])
def welcome_message():
    return "Welcome Back"

app.register_blueprint(profiles_api, url_prefix="/profiles")
app.register_blueprint(auth_api, url_prefix="/auth")

if __name__ == "__main__":
    app.run(debug = True)