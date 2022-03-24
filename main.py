from flask import Flask, request
from menu import *
# from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
enviroment = Environment()

@app.get("/")
def root():
    return "Hello World!"


@app.post("/incoming")
def post():
    body = request.form

    sender = body["From"]
    msg = body["Body"]

    enviroment.recv(sender, msg)

    return "Done"
