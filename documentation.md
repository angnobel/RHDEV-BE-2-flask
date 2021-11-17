1)/

description:returns welcome message

function used: def welcome()

Source: main.py

Parameters: None

Response: returns welcome message

eg: Welcome!




2)/profiles/<string:name>/

returns the dictionary of the name and score that matches the name provided in the url

function: get_profile(name)

source: ProfilesAPI.py

Parameters: none

Response: returns dictionary of name and score

eg: returns when <string:name> is replaced with Richard
{
  "name": "Richard", 
  "scores": [5,4,3,2,1]
}




3)/profiles/<string:name>/

creates a dictionary of name and empty list of score and stores it in db.py

function: create_profile(name)

source: ProfilesAPI.py

Parameters: None

Response: after adding the dictionary to the database, return success message

eg: {"message":"success", "status":"200"}




4)/profiles/<string:name>
delete the dictionary that contains the name specified by user

function:delete_profile(name)

source:ProfilesAPI.py

Parameters:None

Response: status message that shows whether the operation is successful.

eg: if there are no dictionaries deleted, {"message":"failure", "status":"400"} is returned
    if there are dictionaries deleted, {"message":"success", "status":"200"} is returned



5)/profiles/scores/<string:name>/

return the specified name and scores above the specified minimum score

function: get_above_minscore(name)

source: ProfilesAPI.py

Parameters: minScore

Response: if the data requested exists in the database, it will be presented in json. otherwise there will be error message

eg: successful response             failed response
{                                   {"message":"failure", "status":"400"}
  "name": "Richard", 
  "scores": [4,5]
}



6)/auth/register/<string:username>/<string:password>/
adds a user name and hashed password to database

function: register_user(username,password)

source: AuthAPI.py

Parameter: None

Response: if there is a password entered, it returns a success message; otherwise it returns failure message

eg: successful response                     failed response
{"message":"success", "status":"200"}       {"message":"failure", "status":"400"}

7)/login/<string:username>/<string:password>/
match the username and password to a pre-existing username and password in the database, if there is a match, return a token and a success message. Otherwise return a failed message.

function: user_login(username,password)

source: AuthAPI.py

Parameter: None

Response: success message + token         
{
  "message": "success", 
  "status": "200", 
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InNoYXduIiwiaGFzaGVkUGFzc3dvcmQiOjUyMDE4ODg3Njk4ODY0NjI5MjF9.mQZZnZ27x08CvwCP_KBZHPYlxaqWWeba3EJUi49Y2wQ"
}
  or              
  failure message
  {
  "message": "failure", 
  "status": "401"
}



