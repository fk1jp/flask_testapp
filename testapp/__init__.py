from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/echo_bot", methods=['POST'])
def hello_world():
    return request.data

@app.route("/hoge")
def hoge():
    return "hogehoge world!"
