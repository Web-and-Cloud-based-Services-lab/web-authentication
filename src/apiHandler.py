import pymongo
from dbClient import mongo_client
from jwtHandler import jwtHandler
import json

class ApiHandler(object):
    def __init__(self):
        self.client = mongo_client
        self.db = self.client.url_shortener
        self.collection_urls = self.db.Urls
    
    def verify_signiture(self,token):
        encoded_header, encoded_payload, encoded_signature = token.split('.')
        try:
             # decode the base64url encoded string into a byte string, then decode it into a string
            # the payload is of the form: {"name": "<username>"}
            payload = jwtHandler.decode_base64url(encoded_payload).decode()
            # convert the payload string into a json object    
            user_name = json.loads(payload)['name']
        except:
            return {"verified": False, "message": "Invalid payload"}

        try:
            # decode the signature in the request into a byte string
            signature = jwtHandler.decode_base64url(encoded_signature)
        except: 
            return {"verified": False, "message": "Invalid signature"}
        # generate the expected signature in the form of byte string based on the username
        correct_signature = jwtHandler.generate_expected_signature(user_name)

        if signature == correct_signature:
            return {"verified": True, "username": user_name}
        else:
            return {"verified": False, "message": "Invalid signature"}

apiHandler = ApiHandler()