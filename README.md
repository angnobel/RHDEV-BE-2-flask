# Main

## GET /

Homepage that returns a welcome message.  

**Function used:** `main()`  
**Source:** main.py 

**Parameters:** None 

**Response:** String containing welcome message  
Example: 
```
Hello, and welcome!
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

**Response:** String containing new profile's name  
Example: 
```
{
    "status": "success",
    "new_profile": "charles"
}
```

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
{
    "status": "error",
    "message": "profile not found"
}
```

---

## DELETE /profiles/{id}<br>

Deletes the input profile from the database if it exists.  

**Function used:** `profiles_id(id)`  
**Source:** ProfilesAPI.py 

**Parameters:** None  

**Response:** Success status code upon deletion, or error message if profile not found.  
**Example:**   
```
{
    "status": "success"
}
```  
```
{
    "status": "error"
    "message": "profile not found",
}
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
{
    "scores": [
        5,
        4
    ],
    "status": "success"
}
```  
```
{
    "message": "profile not found",
    "status": "error"
}
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
{
    "status": "success",
}
```
```
{
    "status": "error",
    "message": "invalid body"
}
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
{
    "status": "success",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImNoYXJsZXMiLCJwYXNzd29yZEhhc2giOiIxMjM0NSJ9.OWBiNWvJ1_9EKUCfnj-HxdnfKYA-_Uf4Bl_jrWtUc3U"
}
```
```
{
    "status": "error",
    "message": "invalid body"
}
```