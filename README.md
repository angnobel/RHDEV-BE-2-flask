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

# Main

## GET /

Homepage that returns a welcome message.  

**Function used:** `main()`  
**Source:** main.py 

**Parameters:** None 

**Response:** String containing welcome message  
Example: 
```
Welcome User!
```  

---


# Profiles

## GET /profiles<br>

Returns all profiles that exist in the database.

**Function used:** `profiles()`  
**Source:** ProfilesAPI.py 

**Parameters:** None  

**Response:** List of JSON objects  
**Example:**   
```
{  
    "profiles": [  
        {  
            "name": "Nobel",  
            "scores": [  
                1,  
                2,  
                3,  
                4,  
                5  
            ]  
        },  
        {  
            "name": "Richard",  
            "scores": [  
                5,  
                4,  
                3,  
                2,  
                1  
            ]  
        }  
    ],  
    "status": "success"  
}
```  

---

## POST /profiles<br>  

Creates a new profile in the db.

**Function used:** `profiles()`  
**Source:** ProfilesAPI.py 

**Parameters:**   

<table>
    <tr>
        <td>name (required)</td>
        <td> String </td>
        <td> Name of the new profile</td>
    </tr>
</table> 

**Response:** Dict containing new profile's name generated  
---
"Profile created"
---

## GET /profiles/{id}<br>

Checks if the searched profile exists in the database.  
Returns the profile and its associated data if it exists.

**Function used:** `profiles_id(id)`  
**Source:** ProfilesAPI.py 

**Parameters:** None  

**Response:** JSON object of the found profile, or error message if profile not found.  
**Example:**   
```
{
    "data": {
        "name": "Nobel",
        "scores": [
            1,
            2,
            3,
            4,
            5
        ]
    },
    "status": "success"
}
```  
```
"Wrong id"
```

---

## DELETE /profiles/{id}<br>

Deletes the input profile from the database if it exists.  

**Function used:** `profiles_id(id)`  
**Source:** ProfilesAPI.py 

**Parameters:** None  

**Response:** Sends message for user to make sure that the user knows that once deleted profiles cannot be restored. 
Then checks if what the User types in  is found in the database, if successful, success message is given, otherwise error
message is given
**Example:**   
```
User has been deleted
```  
```
User does not exist
```

---

## GET /profiles/{id}/score<br> GET /profiles/{id}/score?minScore={minScoreValue}<br>   

Returns the scores of the input profile from the database if it exists.  
Accepts optional query parameter minScore, which returns all scores above minScore for the input profile.

**Function used:** `profiles_score(id)`  
**Source:** ProfilesAPI.py 

**Parameters:**  
<table>
    <tr>
        <td> minScore (optional)</td>
        <td> String </td>
        <td> Minimum score, for which only scores above it will be returned</td>
    </tr>
</table>  

**Response:** List of scores, or error message if profile not found.  
**Example:**   
```
(3, 4, 5)
```  
```
No scores are found
```

---


# Auth  

## POST /register<br>  

Stores a username and hashedPassword in a local array.

**Function used:** `register()`  
**Source:** AuthAPI.py 

**Parameters:**   

<table>
    <tr>
        <td> username (required)</td>
        <td> String </td>
        <td> Username of user</td>
    </tr>
    <tr>
        <td> passwordHash (required)</td>
        <td> String </td>
        <td> Hash of user password</td>
    </tr>
</table> 

**Response:** Success message upon successful registration, or error message if invalid body  
Example: 
```
successfully registered
```
```
Error, Invalid body
```

## POST /login<br>  

Checks if provided information is valid and returns a JWT token and success message.

**Function used:** `login()`  
**Source:** AuthAPI.py 

**Parameters:**   

<table>
    <tr>
        <td> username (required)</td>
        <td> String </td>
        <td> Username of user</td>
    </tr>
    <tr>
        <td> passwordHash (required)</td>
        <td> String </td>
        <td> Hash of user password</td>
    </tr>
</table> 

**Response:** JWT token and successful message, or error message if invalid body input
Example: 
```
login successful
```
```
login unsuccessful
```