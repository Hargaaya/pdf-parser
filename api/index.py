from flask import Flask

app = Flask(__name__)

@app.route('/')
def parser():
    return "Hello World!"
