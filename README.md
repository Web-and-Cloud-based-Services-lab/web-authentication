# web-authentication
*Web Services and Cloud-based Systems course Project*

**API Functions:** 
- create user account 
- update user password
- login verification
- validate JWT


**Additional Features:**
- Check login expiry time

### Reference
**JWT:**
JWT official introduction:
[link](https://jwt.io/introduction/)
Python hmac library introduction:
[link](https://docs.python.org/3/library/hmac.html)

## Prerequisites

1. `Docker`  installed
2. `Python >= 3.4`  installed

## Build

<!-- ### 1. Run the database

#### Pull `MongoDb` official image from docker

Run the following command to pull MongoDB

```bash
$ docker pull mongo:4.4.6
```

#### Run database

Run the following command to create a container

```bash
$ docker run --name mongo -p 27017:27017 -d mongo:4.4.6
``` -->

### 2. Run the Server

After successfully installed these modules, enter  directory `/src` , run the python file `run.py`

```bash
$ python3 run.py
```

## Server API
| API | Parameter | Method | Example| Description |
| :--- | :---- | :---: |:---|:---|
| / |/ |  GET   | 127.0.0.1:7777 | Server connected information|
/users |[?username=...&password=...] |POST|127.0.0.1:7777/users?username=test&password=test|create a user account|
/users|[?username=...&old-password=...&new-password=...]|PUT|127.0.0.1:7777/users?username=test&old-password=test&new-password=newtest| Update passowrd|
/users/login | [?username=...&password=...]| POST| 127.0.0.1:7777/users/login?username=test&password=test | Login and get JWT| 
/users/validation |[?jwt=...]| GET | 127.0.0.1:7777/users/validation?jwt=eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJuYW1lIjogIkNhaSJ9.MK_ds0u2DsMteRixl1SX1IdInRd73j1p3qNQFOW7yG4| Validate login status and get username|


