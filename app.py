# Python Program to Get IP Address
import socket
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    #print("Your Computer Name is:" + hostname)
    #print("Your Computer IP Address is:" + IPAddr)
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return "<p>Your Computer Name is:" + hostname+"</p>"+"Your Computer IP Address is:" + IPAddr