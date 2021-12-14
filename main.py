from Auth.AuthAPI import auth_api
from Profiles.ProfilesAPI import profiles_api
from flask import Flask
from db import *
from secretkeys import *
import jwt


# Write your flask code here

app = Flask(__name__)

app.config['SECRET_KEY'] = auth_secret_key
app.register_blueprint(profiles_api, url_prefix="/profiles")
app.register_blueprint(auth_api, url_prefix="/auth")

# Endpoints
@app.route("/", methods=["GET"])
def hello():
	return "Welcome!"

# Start the server (developement)
if __name__ == "__main__":
    app.run("localhost", port=8080) #Testing on own computer
	#app.run("0.0.0.0", port=8080) #Deploying