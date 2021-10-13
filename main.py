from Auth.AuthAPI import auth_api
from Profiles.ProfilesAPI import profiles_api
from flask import Flask


# Write your flask code here

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Welcome</p>"

app.register_blueprint(profiles_api, url_prefix="/profiles")
app.register_blueprint(auth_api, url_prefix="/auth")
