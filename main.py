from Auth.AuthAPI import auth_api
from Profiles.ProfilesAPI import profiles_api
from flask import Flask
from db import db


# Write your flask code here

app = Flask(__name__)

app.register_blueprint(profiles_api, url_prefix="/profiles")
app.register_blueprint(auth_api, url_prefix="/auth")

@app.route("/", methods = ['GET'])
def welcome_message():
    return "Good day filthy peaasant!"

if __name__ == "__main__":
    app.run("localhost", port=8080) # Testing on own computer
	app.run("0.0.0.0", port=8080) # Deploying