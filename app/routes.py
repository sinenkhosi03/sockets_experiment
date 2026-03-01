from flask import Blueprint, render_template, url_for, redirect, request
from socket import socket, AF_INET, SOCK_STREAM

serverName = "bore.pub"
serverPort = 37907

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/server_response", methods=["GET", "POST"])
def serverResponse():
    modifiedPhrase = ""
    if request.method == "POST":
        clientSocket = socket(AF_INET, SOCK_STREAM)  # TCP
        phrase = request.form["phrase"]
        print(phrase)
        clientSocket.connect((serverName, serverPort))  # TCP needs connect first
        clientSocket.send(phrase.lower().encode())      # then send
        modifiedPhrase = clientSocket.recv(2048).decode()
        print(modifiedPhrase)
        clientSocket.close()
    return render_template("server_response.html", newPhrase=modifiedPhrase)

@main.route('/return')
def return_home():
    redirect(url_for("main.index"))