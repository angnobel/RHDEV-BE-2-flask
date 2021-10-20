from flask import Flask
from flask import request
from flask import Blueprint
from db import datab

app = Flask(__name__)
# profile = Blueprint('profile',__name__,url_prefix='/profiles')


# @profile.route('/profiles/GET/<string:name>/', methods=['GET'])
@app.route('/profiles/GET/<string:name>/', methods=['GET'])
def get_profile(name):
    GET_profile = {}
    for obj in datab:
        if obj["name"] == str(name):
            GET_profile = {"name" : name , "scores" : obj.get("scores")}
    if GET_profile == {}:
        return "profile does not exist"
    else:
        return GET_profile 

# @profile.route('/profiles/POST/<string:name>/', methods=["POST"])
@app.route('/profiles/POST/<string:name>', methods=["POST", "GET"])
def create_profile(name):
    user_dict ={"name" : name} 
    datab.append(user_dict)
    return f"user {name} has been created"

# @profile.route('/profiles/DELETE/<string:name>', methods=["DELETE","GET"])
@app.route('/profiles/DELETE/<string:name>', methods=["DELETE","GET"])
def delete_profile(name):
    unwanted_profile_list = list(filter(lambda a: a["name"] == name, datab))
    if unwanted_profile_list !=[]:
        datab.remove(unwanted_profile_list[0])
        return f"{name} removed from database"
    else:
        return "name does not exist"


# @profile.route('/scores/GET/<string:name>/', methods=['GET' , 'POST'])
@app.route('/scores/GET/<string:name>/', methods=['GET' , 'POST'])
def get_above_minscore(name):
    minscore = request.args.get('minScore',type=int,default=0)
    score_list = []
    for obj in datab:
        if obj["name"] == str(name):
            score_list = list(filter(lambda a : a > minscore, obj["scores"]))
            score_dict = {"name":name, "scores": score_list}
            return score_dict
    if score_list == []:
        return "candidate not found"


if __name__ == "__main__":
    app.run(debug = True)