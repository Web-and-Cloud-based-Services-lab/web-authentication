from base64 import urlsafe_b64encode
import hmac
import json

class JWTHandler(object):
    def __init__(self, user):
        # the algorithm used to generate the signature is HMAC SHA256
        self.header = {"alg": "HS256", "typ": "JWT"}
        # the payload contains the subject's username, which is an immutable identifier for the user
        self.payload = {"sub": "{}".format(user)}
        # the secret key used to sign the JWT
        self.secret = "Group8Secret"

    # encode header, payload, and signature respectively and generate corresponding JWT
    # reference: https://jwt.io/introduction/ , https://docs.python.org/3/library/hmac.html
    def generate_jwt(self):
        encoded_header = urlsafe_b64encode(json.dumps(self.header).encode()).decode().rstrip('=') 
        encoded_payload = urlsafe_b64encode(json.dumps(self.payload).encode()).decode().rstrip('=')
        # digest() returns the generated signature as a byte string
        signature = hmac.new(self.secret.encode(), (encoded_header + "." + encoded_payload).encode(), "SHA256").digest()
        encoded_signature = urlsafe_b64encode(signature).decode().rstrip('=')
        return encoded_header + "." + encoded_payload + "." + encoded_signature


jwtHandler = JWTHandler("Yuna")
print(jwtHandler.generate_jwt())
