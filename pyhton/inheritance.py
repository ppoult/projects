from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inheritance_1():
    return render_template("inheritance_1.html")

@app.route("/inheritance_2")
def inheritance_2():
    return render_template("inheritance_2.html")
