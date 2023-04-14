
from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from jwtHandler import jwtHandler
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
        
@app.route('/users', methods=["PUT"])
@cross_origin()
def update_password(): 
    get_data=request.args
    get_dict = get_data.to_dict()
    username = get_dict['username']
    old_password = get_dict['old-password']
    new_password = get_dict['new-password']
        
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
        encoded_header, encoded_payload, encoded_signature = token.split('.')
        # decode the base64url encoded string into a byte string, then decode it into a string
        # the payload if of the form of {"name": "<username>"}
        payload = jwtHandler.decode_base64url(encoded_payload).decode()
        # convert the payload string into a json object    
        user_name = json.loads(payload)['name']
        # decode the signature in the request into a byte string
        signature = jwtHandler.decode_base64url(encoded_signature)
        # generate the expected signature in the form of byte string based on the username
        correct_signature = jwtHandler.generate_expected_signature(user_name)
        if signature == correct_signature:
            return {"message": "Authentication Successful", "name": user_name}, 200
        else:
            return {"message": "Authentication Failed", "signature": correct_signature}, 401