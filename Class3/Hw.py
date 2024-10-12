from flask import Flask, url_for

app = Flask(__name__, static_folder="static", static_url_path="/static")

app.run() 