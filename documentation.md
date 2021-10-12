# RHDEV-BE-2-flask Documentation
1. GET /  
  
    Get a welcome message.  
      
    **Function used**: hello()  
    **Source**: /**main.py (line 18)**
    ***  
    **Parameters**: None  
    ***  
    **Reponse**: Welcome Message 
    ***  
    **Example**: /  
    ```
    Welcome! 
    ```

2. GET /profiles/\<int:id\>  

    Get the name and scores associated with that profile based on a given ID.  
    
    **Function used**: get_id()  
    **Source**: /**ProfilesAPI.py (line 10)**
    ***
    **Parameters**: 
    ***
    **Response**: JSON object
    ***
    **Example**: /profiles/1 
    ``` json
    {
        "data": {
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
    ```
3. POST /profiles/create_profile

    Create a new profile with name only.

    **Function used**: add_new_profile()  
    **Source**: /**ProfilesAPI.py (line 20)**
    ***
    **Parameters**:  

        name (required)

    Name of profile added
    ***
    **Response**: String of Response
    ***
    **Example**: /profiles/create_profile
    ```json
    {
        "added": {
            "name": "Eugene",
            "scores" : [],
        },
        "Status": "success"
    }
    ```

    Otherwise, error will be thrown accordingly

4. DELETE /profiles/\<int:id\>

    Delete profile based on id.

    **Function used**: delete_profile()
    **Source**: /**ProfilesAPI.py (line 31)**
    ***
    **Parameters**:
    ***
    **Response**:   String of response
    ***
    **Example**: /profiles/1 
    ```json
    {
        "deleted": {
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
    ```
    Otherwise, error will be thrown accordingly

4. GET /profiles/\<int:id\>/score

    Get all of the scores of a profile above a specified minimum score.

    **Function used**: get_scores_above_min()  
    **Source**: /**ProfilesAPI.py (line 41)**
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
        "data": [
            5,
            4
        ],
        "status": "success"
    }
    ```
    Otherwise, error will be thrown accordingly
6. POST /auth/register

    Stores a username and hashedPassword in an array of credentials.

    **Function used**: register()
    **Source**: /**AuthAPI.py (line 15)**
    ***
    **Parameters**:

        username (Required)
    
    Username of user to register

        passwordHash (Required)
    
    Password of user 
    ***
    **Response**: String of response
    ***
    **Example**: /auth/register?username=eugene&passwordHash=abcdefg123
    ```json
    {
        "message": "registered",
        "status": "success"
    }
    ```
7. POST /auth/login
    
    Checks if credentials are of registered users. 

    **Function used**: login()
    **Source**: /**AuthAPI.py (line 33)**
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
    **Example**: auth/login?username=eugene&passwordHash=abcdefg123
    ```json
    {
        "status": "success",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySUQiOiJCb2IiLCJwYXNzd29yZEhhc2giOiJ5ZXN3ZWNhbiJ9.iG_2s4dHaiDRdWTDRoawtZ8tv_lW8hb7niAzlTmB8n4",
    }
    ```