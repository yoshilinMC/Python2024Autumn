from flask import Flask, url_for, redirect, request
from flask import render_template
from flask import session
import json

app = Flask(__name__)

@app.route("/login")
def login():
    return render_template("index.html")
@app.route("/submit", methods=["POST"])
def submit():
    username = request.values["User"]
    password = request.values["Password"]
    number = request.values["Number"]
    # member = json.dumps({"1":"Amy","2":"Bob","3":"John"})
    if username == "Admin" and password == "123456":
        if number == "1":
            return "Profile page \n Hello Amy"
        elif number == "2":
            return "Profile page \n Hello Bob"
        elif number == "3":
            return "Profile page \n Hello John"
        else :
            return "unavailable ID"
    else :
        return "You're not a member of Admins"


app.run()