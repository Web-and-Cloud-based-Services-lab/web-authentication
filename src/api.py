
from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from apiHandler import apiHandler
from base64 import urlsafe_b64decode
import json

app = Flask(__name__)
cors = CORS(app) # cors is added in advance to allow cors requests
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=["GET"])
@cross_origin()
def index():
    return "Authentication Connected"

@app.route('/users', methods=["POST"])
@cross_origin()
def post_user():
    if request.method == 'POST':
        get_data=request.args # get_data gets the body of post request
        get_dict = get_data.to_dict()
        username = get_dict['username']
        password = get_dict['password']
        if apiHandler.user_exists(username):
            return {"message": "user already exists"},409
        apiHandler.handle_register(username, password)
        return {"message": "account created"}, 201
        
@app.route('/users', methods=["PUT"])
@cross_origin()
def update_password(): 
    get_data=request.args
    get_dict = get_data.to_dict()
    username = get_dict['username']
    old_password = get_dict['old-password']
    new_password = get_dict['new-password']
    if not apiHandler.user_exists(username):
        return {"message": "username does not exist"}, 403
    if not apiHandler.password_validated(username, old_password):
        return {"message": "old password is not valid"}, 403
    apiHandler.handle_password_update(username, new_password)
    return {"message": "password changed"}, 200

@app.route('/users/login', methods=["POST"])
@cross_origin()
def handle_login():
    if request.method == 'POST':
        get_data=request.args
        get_dict = get_data.to_dict()
        username = get_dict['username']
        password = get_dict['password']

@app.route('/users/validation', methods=["POST"])
@cross_origin()
def validation_check():
    if request.method == 'POST':
        get_data=request.args
        get_dict = get_data.to_dict()
        token = get_dict['jwt']

        verify_result = apiHandler.verify_signiture(token)
        if verify_result["verified"]:
            return {"message": "Authentication Successful", "name": verify_result["username"]}, 200
        else:
            return {"message": "Authentication Failed", "type": verify_result["message"]}, 401