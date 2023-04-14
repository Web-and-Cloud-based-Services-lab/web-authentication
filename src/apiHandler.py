from dbClient import mongo_client
from jwtHandler import jwtHandler
import json

class ApiHandler(object):
    def __init__(self):
        self.client = mongo_client
        self.db = self.client.user_auth
        self.user_info = self.db.user_info
        if not self.user_exists("admin"):
            self.user_info.insert_one({"username": "admin", "password": "admin"})

    # retrieve all usernames stored in database
    def get_users(self):
        documents = self.user_info.find({})
        keys = []
        for document in documents:
          keys.append(document['username'])
        return json.dumps(keys, indent=2, ensure_ascii=False)
        
    def user_exists(self, username):
        documents = self.user_info.find({})
        for document in documents:
            if document["username"] == username:
                return True
        return False
    
    def handle_register(self, username, password):
        self.user_info.insert_one({"username": username, "password": password})
    
    def password_validated(self, username, password):
        query = {"username": username}
        document = self.user_info.find_one(query)
        if document == None:
            return False
        return document["password"] == password
        
    def handle_password_update(self, username, new_password):
        query = {"username": username}
        new_value = { "$set": { "password": new_password } }
        self.user_info.update_one(query, new_value)

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