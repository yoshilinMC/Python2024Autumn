from flask import Flask, url_for
from flask import render_template, request

# app = Flask(__name__, static_folder="template", static_url_path="/spring")

# @app.route("/spring/W2.html")
# def index():
#     return render_template("W2.html")

# app.run() 

# app = Flask(__name__)

# @app.route("/spring/class1.html")
# def index(host):
#     return render_template("class1.html", host=host)
# app.run()

# app = Flask(__name__)

# @app.route("/")
# def index():
#     print("請求方法:", request.method)
#     print("通訊協定:", request.scheme)
#     print("主機名稱:", request.host)
#     print("路徑:", request.path)
#     print("完整的網址:", request.url)
#     print("瀏覽器作業系統 : ", request.headers.get("user-agent"))
#     print("語言偏好 : ", request.headers.get("accept-language"))
#     print("引薦網址 : ", request.headers.get("referrer"))
#     return "Hello flask"
# app.run()

# app = Flask(__name__)

# @app.route("/", methods=["GET"])
# def index():
#     name = request.args.get("name")
#     print("使用者名稱是 : ",name)
#     return "Hello Flask"
# app.run()

app = Flask(__name__)

@app.route("/fruit")
def fruit():
    return "<form method='post' action='/submit'> <input type='text' name='username'/> <button type='submit'> Submit</button></form> "
@app.route("/submit", methods=["POST"])
def submit():
    username = request.values["username"]
    return "I like " + username
app.run()

# def a(func):
#     print("makeup...")
#     return func

# def b():
#     print("go!!!")

# b = a(b)
# b()