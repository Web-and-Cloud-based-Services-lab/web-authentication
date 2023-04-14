from base64 import urlsafe_b64encode, urlsafe_b64decode
import hmac
import json

class JWTHandler(object):
    def __init__(self):
        # the algorithm used to generate the signature is HMAC SHA256
        self.header = {"alg": "HS256", "typ": "JWT"}
        # the secret key used to sign the JWT
        self.secret = "Group8Secret"

    # encode header, payload, and signature respectively and generate corresponding JWT
    # reference: https://jwt.io/introduction/ , https://docs.python.org/3/library/hmac.html
    def generate_jwt(self, username):
        # the payload contains the subject's username, which is an immutable identifier for the user
        payload = {"name": "{}".format(username)}
        encoded_header = urlsafe_b64encode(json.dumps(self.header).encode()).decode().rstrip('=') 
        encoded_payload = urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip('=')
        # digest() returns the generated signature as a byte string
        signature = hmac.new(self.secret.encode(), (encoded_header + "." + encoded_payload).encode(), "SHA256").digest()
        encoded_signature = urlsafe_b64encode(signature).decode().rstrip('=')
        return encoded_header + "." + encoded_payload + "." + encoded_signature

    # generate the expected signature in the form of byte string based on the username
    def generate_expected_signature(self, username):
        payload = {"name": "{}".format(username)}
        encoded_header = urlsafe_b64encode(json.dumps(self.header).encode()).decode().rstrip('=') 
        encoded_payload = urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip('=')
        signature = hmac.new(self.secret.encode(), (encoded_header + "." + encoded_payload).encode(), "SHA256").digest()
        return signature
    
    # decode the base64url encoded string into a byte string
    def decode_base64url(self, encoded):
        return urlsafe_b64decode(encoded + "=" * (4 - len(encoded) % 4))

jwtHandler = JWTHandler()
print(jwtHandler.generate_jwt("Yuna"))
print(jwtHandler.generate_jwt("Fan"))
print(jwtHandler.generate_jwt("Cai"))
