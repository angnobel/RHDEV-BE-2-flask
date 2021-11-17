from flask import Flask
from db import datab
from ProfilesAPI import profile
from AuthAPI import auth_api

app = Flask(__name__)
app.register_blueprint(profile, url_prefix="/profiles")
app.register_blueprint(auth_api, url_prefix="/auth")


@app.route('/', methods=['GET'])
def welcome():
    return 'welcome!'

if __name__ == "__main__":
    app.run(debug=True)