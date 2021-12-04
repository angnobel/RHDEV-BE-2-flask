# Simulated ExamScore API Documentation

## Profile API

1. **GET** /profiles/<int:id>

  - **Description:** To retrieve the information (name and score) of a profile.

  - **Function used:** getProfile()

  - **Source:** /Profiles/ProfilesAPI.py (Line 9)

  - **Parameter(s):** 

    - ```id``` (required, must be an integer), the ID of the desired profile.

  - **Request body:** None, only parameter on endpoint needs to be provided.

  - **Response(s):** 

    - Success (200)

      ```python
      {
       "status": "success", 
       "profile": 
       	{"name": "Nobel", 
       	 "scores": [1, 2, 3, 4, 5]
      	}
      }
      ```

    - Fail

      ```python
      {
       "status": "fail", 
       "message": "Profile not found."
      }
      ```

2. **POST** /profiles/

  - **Description:** To add a new profile into the database.

  - **Function used:** addProfile()

  - **Source:** /Profiles/ProfilesAPI.py (Line 19)

  - **Parameter(s):** None

  - **Request body:** 

    ```python
    {
     "name": "string" 
    }
    ```

  - **Response(s):** 

    - Success (200)

      ```python
      {
       "status": "success", 
       "message": "New profile added."
      }
      ```

    - Fail

      ```python
      {
       "status": "fail", 
       "message": "Profile not found."
      }
      ```

3. **DELETE** /profiles/<int:id>

   - **Description:** To remove an existing profile from the database.

   - **Function used:** deleteProfile()

   - **Source:** /Profiles/ProfilesAPI.py (Line 27)

   - **Parameter(s):** 

     - ```id``` (required, must be an integer), the ID of the desired profile.

   - **Request body:** None, only parameter on endpoint needs to be provided.

   - **Response(s):** 

     - Success (200)

       ```python
       {
        "status": "success", 
        "message": "Profile deleted."
       }
       ```

     - Fail

       ```python
       {
        "status": "fail", 
        "message": "Profile not found."
       }
       ```

4. **GET** /profiles/<int:id>/score

   - **Description:** To retrieve the scores of a profile which are greater or equal to the minimum score provided by the requester.

   - **Function used:** getMinScore()

   - **Source:** /Profiles/ProfilesAPI.py (Line 37)

   - **Parameter(s):** 

     - ```id``` (required, must be an integer), the ID of the desired profile.
     - ```minScore``` (optional, must be an integer), the minimum score, given as an argument.

   - **Request body:** None, only parameter on endpoint needs to be provided.

   - **Response(s):** 

     - Success (200)

       ```python
       {
        "status": "success", 
        "scores": [3, 4, 5]
       }
       ```

     - Fail

       ```python
       {
        "status": "fail", 
        "message": "Profile not found."
       }
       ```

## Authentication API

1. **POST** /auth/register

   - **Description:** To register a new credential for API access.

   - **Function used:** Register()

   - **Source:** /Auth/AuthAPI.py (Line 13)

   - **Parameter(s):** None

   - **Request body:**

     ```python
     {
      "username": "string"
      "passwordHash": "string"
     }
     ```

   - **Response(s):** 

     - Success (200)

       ```python
       {
        "status": "success", 
        "message": "Credentials successfully registered."
       }
       ```

     - Fail (no username provided)

       ```python
       {
        "status": "fail",
        "message": "No username."
       }
       ```

     - Fail (no password [hash] provided)

       ```python
       {
        "status": "fail",
        "message": "No password."
       }
       ```

2. **POST** /auth/login

   - **Description:** To authorise a credential holder to access the API.

   - **Function used:** Login()

   - **Source:** /Auth/AuthAPI.py (Line 33)

   - **Parameter(s):** None

   - **Request body:**

     ```python
     {
      "username": "string"
      "passwordHash": "string"
     }
     ```

   - **Response(s):** 

     - Success (200)

       ```python
       {
        "status": "success", 
        "message": "Login successful."
       }
       ```

     - Fail (401 Not authenticated)

       ```python
       {
        "status": "fail",
        "message": "Authentication failed."
       }
       ```

     - Fail (No username provided)

       ```python
       {
        "status": "fail",
        "message": "No username."
       }
       ```

     - Fail (No password provided)

       ```python
       {
        "status": "fail",
        "message": "No password."
       }
       ```

     - Fail (bad token)

       ```python
       {
        "status": "fail",
        "message": "Bad token"
       }
       ```

​				
