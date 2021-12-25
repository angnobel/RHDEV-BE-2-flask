from flask import Flask
from Profiles.ProfilesAPI import profiles_api
from db import db
from Auth.AuthAPI import auth_api
app = Flask(__name__)


################################
#    1. Homepage endpoint      #
################################
@app.route("/", methods=["GET"])
def welcome():
    return "<h1> Welcome! </h1>"

################################
#       2. id endpoint         #
################################
app.register_blueprint(profiles_api, url_prefix="/profiles")
app.register_blueprint(auth_api, url_prefix="/auth")

################################
#   3. Used to run webpages    #
################################
if __name__ == "__main__":
    app.run("localhost", port=5000) 









