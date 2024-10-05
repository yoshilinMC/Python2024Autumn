from flask import Flask

app  = Flask(__name__) 

@app.route("/Yoshi")
def home():
    return "<h1>2024 Autumn</h1>\n<h3>Learn Flask</h3>"
app.run() # 執行