from os import environ
from flask import request
from dotenv import dotenv_values

def verify_token():
    provided_token = request.headers.get("token")
    secret_token = environ.get('TOKEN') or dotenv_values(".env").get("TOKEN")
    
    if provided_token != secret_token:
        raise Exception("token is not valid")
    else:
        return None