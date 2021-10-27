 RHDEV-BE-2-flask
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
# RHDEV-BE-2-flask Documentation
1. GET /  

    Get a welcome message.  

    **Function used**: hello_world()  
    **Source**: /**main.py (line 17)**
    ***  
    **Parameters**: None  
    ***  
    **Reponse**: Welcome message  
    ***  
    **Example**: /  
    ```
    Welcome to the database! 
    ```

2. GET /profiles/\<int:id\>  

    Get the name and scores of the profile based on a given ID.  

    **Function used**: get_details()  
    **Source**: /**ProfilesAPI.py (line 11)**
    ***
    **Parameters**: None
    ***
    **Response**: JSON object
    ***
    **Example**: /profiles/1 
    ``` json
    {
        "Data": {
            "name": "Richard",
            "scores": [
                5,
                4,
                3,
                2,
                1
            ]
        },
        "Status": "Success"
    }
    ```
3. POST /profiles/profiles

    Create a new profile with a name only.

    **Function used**: add_details()  
    **Source**: /**ProfilesAPI.py (line 25)**
    ***
    **Parameters**:  

        name (required)

    Name of profile added
    ***
    **Response**: String of Response
    ***
    **Example**: /profiles/profiles
    ```json
    {
        "Added": {
            "name": "Govin"
        },
        "Status": "Success"
    }
    ```

    Otherwise, errors will be given back to user accordingly

4. DELETE /profiles/\<int:id\>

    Delete a profile based on the id given.

    **Function used**: get_details()
    **Source**: /**ProfilesAPI.py (line 11)**
    ***
    **Parameters**: None
    ***
    **Response**:   String of response
    ***
    **Example**: /profiles/1 
    ```json
    {
        "Deleted": {
            "name": "Richard",
            "scores": [
                5,
                4,
                3,
                2,
                1
            ]
        },
    "Status": "Success"
    }
    ```
    Otherwise, errors will be given back to user accordingly

4. GET /profiles/\<int:id\>/score

    Get all of the scores of a profile above a specified minimum score.

    **Function used**: get_min_score()  
    **Source**: /**ProfilesAPI.py (line 36)**
    ***
    **Parameters**:

        minScore

    Get scores of the specified profile based on the given id above minScore. If minScore is not specified, returns all scores. 
    ***
    **Response**: List of scores
    ***
    **Example**: /profiles/1/score?minScore=3
    ```json
    {
        "Data": [
            5,
            4
        ],
        "Status": "Success"
    }
    ```
    Otherwise, errors will be given back to user accordingly
6. POST /auth/register

    Stores a username and a hashed password in a list of credentials.

    **Function used**: register()
    **Source**: /**AuthAPI.py (line 12)**
    ***
    **Parameters**:

        username (Required)

    Username of user to register

        passwordHash (Required)

    Password of user 
    ***
    **Response**: String of response
    ***
    **Example**: /auth/register?username=govin&passwordHash=abcde123
    ```json
    {
        "Message": "Successfully registered",
        "Status": "Success"
    }
    ```
7. POST /auth/login

    Checks if credentials are of registered users. 

    **Function used**: register()
    **Source**: /**AuthAPI.py (line 19)**
    ***
    **Parameters**:

        username 

    Username of user to register

        passwordHash 

    Password of user 

        token

    JWT token to verify login
    ***
    **Response**: If JWT token is not provided, returns JWT token. In other cases, returns string of response
    ***
    **Example**: auth/login?username=govin&passwordHash=abcde123
    ```json
    {
        "Status": "Success",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imp1c3RpbiIsInBhc3N3b3JkSGFzaCI6ImFiY2RlZmcxMjMifQ.X7VZq1-kMeyA8UDIFD_pvR5-sKrMR9YLXHVPwEuReek"
    }
    ```