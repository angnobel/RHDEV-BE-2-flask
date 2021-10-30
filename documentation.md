Profile API: 

1) GET (profiles/<int:userID>)
This will retrieve a user's profile. 
Function used: retrieve_profile():
Source: /Profiles/ProfilesAPI.py (Line 10)
Parameters: 
    userID (required)
        ID of user
Response: Profile of the user with list of scores
Example: /profiles/1
{
    "message": {
        "name": "Richard",
        "scores": [
            5,
            4,
            3,
            2,
            1
        ]
    },
    "status": "success"
}

2) POST (profiles/)
This will register a user. Name of the user has to be supplied. It will initialise the profile for the user and return a success message upon creation.
Function used: create_profile()
Source: /Profiles/ProfilesAPI.py (Line 29)
Parameters: none
Response: Success message
Example: /
{"tatus": "success", "message": "profile added"}

3) DELETE (profiles/<int:userID>)
This will delete a user's profile lazily by replacing the name with "@". 
Function used: delete_profile()
Source: /Profiles/ProfilesAPI.py (Line 37)
Parameters: 
    userID (required)
        ID of user
Response: Success message
Example: /profiles/1
{
    "message": "profile deleted",
    "status": "success"
}

4) GET (profiles/<int:userID>/score)
This is a description
Function used: get_min_score()
Source: /Profiles/ProfilesAPI.py (Line 51)
Parameters: 
    userID (required)
        ID of user
    min_score (optional)
        minimum score to be displayed
Response: Scores from profile, with the option to display only scores greater than a provided number. 
Example: /profiles/0/score?minScore=3
{
    "data": {
        "scores": [
            3,
            4,
            5
        ]
    },
    "status": "success"
}

------------------------------------------------------------

Authentication API: 

5) POST (auth/register)
This is a description
Function used: 
Source: /Auth/AuthAPI.py (Line X)
Parameters: userID
Response: Success message
Example:

6) POST (auth/<int:userID>)
This is a description
Function used: 
Source: /Auth/AuthAPI.py (Line X)
Parameters: userID
Response: Success message
Example:

