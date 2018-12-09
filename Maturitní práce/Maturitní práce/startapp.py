# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#from flask_mail import Mail, Message

from flask import Flask, render_template, request, url_for

app = Flask(__name__)

app.config["MAIL_SERVER"]="smtp.gmail.com"
app.config["MAIL_PORT"]=465
app.config["MAIL_USE_SSL"]=True
app.config["MAIL_USERNAME"]="zacpalweb@gmail.cz"
app.config["MAIL_PASSWORD"]="kavanata123"

#mail= Mail(app)

@app.route("/index/")
def index():
    return render_template("index.html")

@app.route("/omne/")
def omne():
    return render_template("omne.html")

@app.route("/clanky/")
def clanky():
    return render_template("clanky.html")

@app.route("/kontakt/")
def kontakt():
    return render_template("kontakt.html")


@app.route("/zprava/")
def zprava():
    try:
        msg=Message("Ahoj",sender="zacpalweb@gmail.com",recipients=["zacpalweb@gmail.com"])
        msg.body="Tak co??"
        mail.send(msg)
        return "Message sent!"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)