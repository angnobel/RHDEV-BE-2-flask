from Auth.AuthAPI import auth_api
from Profiles.ProfilesAPI import profiles_api
from flask import Flask
from db import db

app = Flask(__name__)

app.register_blueprint(profiles_api, url_prefix="/profiles")
app.register_blueprint(auth_api, url_prefix="/auth")

# Write your flask code here



#/welcome/ is the URL endpoint, method accepted is GET
@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to the Home Page!"

if __name__ == "__main__":
    app.run(debug=True)
