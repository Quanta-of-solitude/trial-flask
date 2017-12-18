from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import myjson
import json


app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('home.html')
    else:
        return "Hello Empty place._.!  <a href='/logout'>Logout</a>"

@app.route('/flogin', methods=['POST', 'GET'])
def flogin():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Empty place._.!  <a href='/logout'>Logout</a>"

@app.route('/login', methods=['POST'])
def do_admin_login():
    url = "{}".format(os.environ.get("link_to_me"))
    data = myjson.get(url)
    data = json.loads(data)
    print(data["name"])
    if request.form['password'] == data["password"] and request.form['username'] == data["name"]:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return flogin()



@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route("/commands")
def all_commands():
    return render_template("commands.html")

@app.route("/commands/general")
def general():
    return render_template("general_help.html")

@app.route("/commands/ae")
def aestuff():
    return render_template("ae_help.html")

@app.route("/commands/translator")
def translation():
    return render_template("translator_help.html")

@app.route("/commands/moderation")
def moderation():
    return render_template("moderation_help.html")

@app.route("/commands/weleave")
def weleave():
    return render_template("wel_help.html")

@app.route("/commands/miscellaneous")
def misc():
    return render_template("misc_help.html")


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run()
