# RHDEV-BE-2-flask Documentation
1. GET /  
  
    Get a welcome message.  
      
    **Function used**: hello_world()  
    **Source**: /**main.py (line 15)**
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

    Get the name and scores associated with that profile based on a given ID.  
    
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
3. POST /profiles/

    Create a new profile with name only.

    **Function used**: add_details()  
    **Source**: /**ProfilesAPI.py (line 23)**
    ***
    **Parameters**:  

        name (required)

    Name of profile added
    ***
    **Response**: String of Response
    ***
    **Example**: /profiles/
    (form-body) name=Justin
    ```json
    {
        "Added": {
            "name": "Justin"
        },
        "Status": "Success"
    }
    ```

    Otherwise, error will be thrown accordingly

4. DELETE /profiles/\<int:id\>

    Delete profile based on id.

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
    Otherwise, error will be thrown accordingly

4. GET /profiles/\<int:id\>/score

    Get all of the scores of a profile above a specified minimum score.

    **Function used**: get_min_score()  
    **Source**: /**ProfilesAPI.py (line 32)**
    ***
    **Parameters**:

        minScore
    
    Get scores of the specified profile based on the given id above minScore. If minScore is not specified, returns all scores. 
    ***
    **Response**: List of scores
    ***
    **Example**: /profiles/1/score

    (form-body) minScore=3
    ```json
    {
        "Data": [
            5,
            4
        ],
        "Status": "Success"
    }
    ```
    Otherwise, error will be thrown accordingly
6. POST /auth/register

    Stores a username and hashedPassword in an array of credentials.

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
    **Example**: /auth/register
    
    (form-body) username=justin passwordHash=abcdefg123
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
    **Example**: auth/login 
    
    (form-body) username=justin passwordHash=abcdefg123
    ```json
    {
        "Status": "Success",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imp1c3RpbiIsInBhc3N3b3JkSGFzaCI6ImFiY2RlZmcxMjMifQ.X7VZq1-kMeyA8UDIFD_pvR5-sKrMR9YLXHVPwEuReek"
    }
    ```