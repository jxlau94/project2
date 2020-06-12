import os

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        name = request.form.get("name")
    else:
        name = "my friend"
    return render_template("index.html",name=name)


'''
@app.route("/channel", methods=["POST"])
def channel():
    name=request.form.get("name")
    return render_template("channel.html",name=name)
'''

