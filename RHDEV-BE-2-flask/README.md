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
