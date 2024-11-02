from flask import Flask, url_for
from flask import render_template, request

app = Flask(__name__, static_folder="template", static_url_path="/investigation")

@app.route("/investigation/Hw3.html")
def investigate():
    return render_template("Hw3.html")
@app.route("/submit", methods=["POST"])
def submit():
    username = request.values["username"]
    Email = request.values["Email"]
    favorite = request.values["favorite"]
    comments = request.values["comments"]
    interest = request.values["interest"]
    return "表單繳交成功 ! 您的資料如下 : \n 姓名 : {} \n 信箱 : {} \n 最有興趣的項目 : {}" .format(username,Email,favorite)

app.run()