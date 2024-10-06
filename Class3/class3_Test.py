from flask import Flask, url_for

app = Flask(__name__, static_folder="static", static_url_path="/static")

# 路由設定
@app.route("/")
def index():
    return "Welcome to my Web!" 

@app.route("/Member/<name>") 
def sayHi(name):
    return "Hi, our member : "+name

@app.route("/Admin/<level>") 
def login(level):
    if level=="A":
        return"Login here" 
    if level=="B":
        return "<h1>You're not available in here</h1>" 
app.run() 