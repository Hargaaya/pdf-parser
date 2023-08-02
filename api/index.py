import sys
from utils.token import verify_token
from flask import Flask, jsonify

app = Flask(__name__)

@app.before_request
def check_token_callback():
    try:
        verify_token()
        
    except(Exception):
        return jsonify(error = "missing a valid token"), 401

@app.route('/')
def parser():
    return jsonify(data = "Hello World!")
