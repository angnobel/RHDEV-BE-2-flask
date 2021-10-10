from Auth.AuthAPI import auth_api
from Profiles.ProfilesAPI import profiles_api
from flask import Flask
from db import db
from secret import SECRET_KEY


# Write your flask code here

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY

app.register_blueprint(profiles_api, url_prefix="/profiles")
app.register_blueprint(auth_api, url_prefix="/auth")

@app.route("/", methods=["GET"])
def main():
    return "Hello, and welcome!" 

if __name__ == "__main__":
    # Development
    app.run("localhost", port=8080)