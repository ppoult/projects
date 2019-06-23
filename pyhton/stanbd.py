import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def bdchecker():
    now = datetime.datetime.now()
    stanbd = now.month == 1 and now.day == 5
    return render_template("isitstanbd.html", stanbd=stanbd)
