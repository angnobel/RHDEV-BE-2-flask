# RHDEV-BE-2-flask
Homewwork template for BE training lesson 2: Flask and web servers

Setup a basic API to simulate a website that tracks profiles and scores for exams

A simulated db is provided. Note that the db will not be updated between runs
    In main:
GET / homepage that returns a welcome message
    In profiles API (/profiles prefix)
GET /{id} to retrieve the name and all scores of a profile
POST /profiles to create a new profile (name only)
DELETE /{id} to delete a profile
GET /{id}/score?minScore= to retrieve all scores of a profile, above the min score
    In authentication API (/auth prefix)
POST /register stores a username and hashedPassword (given as hashed)
Store it in a local array
Login /login checks if the provided information is valid and return a jwt token + success message

Give a reasonable return format with appropriate status code and messages.
{“message” : “success/fail”, “data”:””}
Also submit a simplified documentation of your API. You can use the format below.



OPTIONALS: 
Add environmental variables into the system (for jwt signing secret)
In the login route, check if jwt token is provided and valid
Assume URL argument has token “?token=sdlkaskdnalsdnsald”
See if username and password field arre present

In Main
1) GET /

Sends a welcome message to user

Function used: Welcome()
Source: main.py

Parameters: None

Response: String containing welcome message

Example: "Welcome to the Home Page!"

2) GET /profiles/

Sends a welcome message to user

Function used: welcome()
Source: profiles.py

Parameters: None

Response: String containing welcome message

Example: "Welcome to the Profiles!"

3) POST /profiles/profiles

Creates a new user profiles

Function used: create_profile()
Source: profiles.py

Parameters: None

Response: Returns JSON object of the profile created or error message if profile already exists

Example: ```{"status":"error", "message":"profile already exists"}``` or ``` {"status":"success","message":"profile created"}```

3) GET /profiles/<int:id>

Retrieves all data stored in a users profile

Function used: retrieve_all_details()
Source: profiles.py

Parameters: None

Response: Returns JSON object of the profile's details or error message if profile doesn't exist

Example: ```{"status":"error", "message":"profile doesn't exists"}``` or ``` {"status":"success","data": {"name": "Nobel", "scores": [1, 2, 3, 4, 5]} }```

4) DELETE /profiles/<int:id>

Deletes a users profile

Function used: delete_profile()
Source: profiles.py

Parameters: None

Response: Returns JSON object of the status, success if profile is deleted or error if the profile doesn't exists

Example: ```{"status":"error", "message":"profile doesn't exists"}``` or ``` {"status":"success","message":"profile deleted"}```

5) GET /profiles/<int:id>/score

Retrieves the scores of a profile above the min score if stated, otherwise it returns all the scores

Function used: retrieve_min_score()
Source: profiles.py

Parameters: None

Response: Returns JSON object of the scores and status, error if profile doesn't exist or method is wrong

Example: ```{"status":"error", "message":"profile doesn't exists"}``` or ``` {"status":"error"}``` or ```{"scores": [9, 29, 34], "status": "success"}``` or ```{"scores": [34], "status": "success"}```

6) POST /auth/register

Stores a username and password given by the user in a local array called 'details' in db

Function used: register()
Source: auth.py

Parameters: None

Response: Returns JSON object of the status, error if password or user field is empty

Example: ```{'status':'error','message':'username or password field is empty'}``` or ```{"status":"success", "message":"user registered"}```

6) POST /auth/login

Checks whether username and password given by the user is valid and returns a jwt token along with status

Function used: login()
Source: auth.py

Parameters: None

Response: Returns JSON object containing the status and jwt token if successful, else it returns an error message if username and password is invalid

Example: ```{'status':'error','message':'username or password entered incorrectly'}``` or ```{'status':'success','token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'}```