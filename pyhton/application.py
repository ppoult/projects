from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, world!</h1>"

@app.route("/Stanley")
def stanb():
    return "<h1>Hello, Stanley!</h1>"

@app.route("/<string:name>")
def genhello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!</h1>"
