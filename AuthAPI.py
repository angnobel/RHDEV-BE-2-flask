import json
import jwt
from flask import Flask, Blueprint, request,jsonify
from db import datab
from db import profile_auth


auth_api = Blueprint('auth_api',__name__,url_prefix='/auth')


@auth_api.route('/register/POST/<string:username>/<string:password>/', methods=['POST','GET'])
def register_user(username,password):
    passwordhash = hash(password)
    user_dict = {"username":username, "hashedPassword": passwordhash}
    if user_dict["hashedPassword"] == -9223363242168321331:
        return jsonify({"message":"failure", "status":"400"})
    else:
        profile_auth.append(user_dict)
        return jsonify({"message":"success", "status":"200"})









# if __name__ == "__main__":
#     app.run(debug=True)

