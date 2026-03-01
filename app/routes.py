from flask import Blueprint, render_template, url_for, redirect, request
from socket import *

serverName="bore.pub"
serverPort = 37907


main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/server_response", methods=["GET", "POST"])
def serverResponse():
    modifiedPhrase = ""
    if request.method =="POST":
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName,serverPort))
        phrase = request.form["phrase"]
        print(phrase)
        clientSocket.send(phrase.lower().encode())
        modifiedPhrase= clientSocket.recvfrom(2048)
        print(modifiedPhrase.decode())
        clientSocket.close()


    return render_template("server_response.html", newPhrase=modifiedPhrase)

@main.route('/return')
def return_home():
    redirect(url_for("main.index"))