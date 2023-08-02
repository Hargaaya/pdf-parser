import os
import sys
import time
from fileinput import filename
from utils.token import verify_token
from flask import Flask, jsonify, request
from py_pdf_parser.loaders import load_file

app = Flask(__name__)

@app.before_request
def check_token_callback():
    try:
        verify_token()
        
    except(Exception):
        return jsonify(error = "missing a valid token"), 401
    
@app.route('/check')
def check():
    return jsonify(data = "Hello world!")

## TODO: Filter parsed content, remove unwanted items
@app.route('/', methods = ['POST'])
def parser():
    f = request.files['pdf']
    fname = str(time.time_ns()) + '-' + f.filename
    f.save(fname)
    
    document = load_file(fname)
    text = ""
    
    for x in document.elements:
        text += x.text()
    
    os.remove(fname)
    
    return jsonify(data = text)
