from flask import Flask,request,Blueprint,jsonify
from db import datab


profile = Blueprint('profile',__name__,url_prefix='/profiles')


@profile.route('/GET/<string:name>/', methods=['GET'])
def get_profile(name):
    GET_profile = {}
    for obj in datab:
        if obj["name"] == str(name):
            GET_profile = {"name" : name , "scores" : obj.get("scores")}
    if GET_profile == {}:
        return jsonify({"message":"failure", "status":"401"})
    else:
        return jsonify(GET_profile) 

@profile.route('/POST/<string:name>/', methods=["POST","GET"])
def create_profile(name):
    user_dict ={"name" : name,"scores": []} 
    datab.append(user_dict)
    return jsonify({"message":"success", "status":"200"})

@profile.route('/DELETE/<string:name>/', methods=["DELETE","GET"])
def delete_profile(name):
    unwanted_profile_list = list(filter(lambda a: a["name"] == name, datab))
    if unwanted_profile_list !=[]:
        datab.remove(unwanted_profile_list[0])
        return jsonify({"message":"success", "status":"200"})
    else:
        return jsonify({"message":"failure", "status":"400"})


@profile.route('/scores/GET/<string:name>/', methods=['GET' , 'POST'])
def get_above_minscore(name):
    minscore = request.args.get('minScore',type=int,default=0)
    score_list = []
    for obj in datab:
        if obj["name"] == str(name):
            score_list = list(filter(lambda a : a > minscore, obj["scores"]))
            score_dict = {"name":name, "scores": score_list}
            return jsonify(score_dict)
    if score_list == []:
        return jsonify({"message":"failure", "status":"400"})

