from flask import Flask
import tasty_analyzer

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
