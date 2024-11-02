from flask import Flask, url_for, redirect
from flask import make_response
from flask import render_template, request
from flask import session
import json

app = Flask(__name__)

# @app.route("/response")
# def response():
#     lang = request.headers.get("accept_language")
#     if lang.startswith("zh"):
#         return json.dumps({"text":"你好"}, ensure_ascii=False)
#     else:
#         return json.dumps({"text":"Hello"}, ensure_ascii=False)

# @app.route("/login")
# def login():
#     return "<form method='post' action = '/submit'> <input type = 'text' name ='username'/> <button type='submit'>Submit</button></form>"
# @app.route("/submit", methods=["POST"])
# def submit():
#     username = request.values["username"]
#     return redirect("https://github.com/"+username)

"""
@app.route("/login")
def Login():
    session["logged_in"] = True
    return "Login success"

@app.route("/logout")
def Login():
    session["logged_in"] = False
    return "Logout success"

@app.route("/profile")
def profile():
    if session.get("logged_in"):
        return "Profile page"
    else :
        return "User not logged in"
"""

app.run()