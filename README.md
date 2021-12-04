# RHDEV-BE-2-flask

A simulated db is provided. Note that the db will not be updated between runs.

    In main:

GET / - Returns a welcome message at homepage

    In profiles API (/profiles prefix):

* GET /{id} - retrieves the name and all scores of a profile
* POST /profiles - creates a new profile (name only)
* DELETE /{id} - deletes a profile
* GET /{id}/score?minScore= to retrieve all scores of a profile, above the minimum score

    In authentication API (/auth prefix):

* POST /register - stores a username and hashedPassword (given as hashed) in a local array
* Login /login - checks if the provided information is valid and return a jwt token + success message if successful, else return a 401 error if failed

