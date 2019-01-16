# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#from flask_mail import Mail, Message

from flask import Flask, render_template, request, url_for

app = Flask(__name__)

app.config.update(dict(
    MAIL_SERVER = 'smtp.googlemail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'zacpalweb',
    MAIL_PASSWORD = '[kavanata123]'
))
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

@app.route("/atheny/")
def atheny():
    return render_template("atheny.html")

@app.route("/process_email", methods=["POST","GET"])
def process_email():
    jmeno=request.form["jmeno"]
    prijmeni=request.form["prijmeni"]
    email=request.form["email"]
    predmet=request.form["predmet"]
    zprava=request.form["zprava"]
    msg = Message(jmeno, prijmeni, email, predmet, zprava, sender='zacpalweb@gmail.com', recipients=['zacpalweb@email.com'])
    mail.send(msg)

    return flash("Děkuji za dotaz, odpovím hned jak to bude možné.")

if __name__ == "__main__":
    app.run(debug=True)
