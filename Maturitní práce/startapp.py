# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import smtplib
#from flask_mail import Mail, Message


from flask import Flask, render_template, request, url_for
from data import Clanky
app = Flask(__name__)
Clanky=Clanky()
app.config.update(dict(
    DEBUG=True,
    MAIL_SERVER = 'smtp.googlemail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'zacpalweb',
    MAIL_PASSWORD = '[kavanata123]'
))
#mail= Mail(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/omne")
def omne():
    return render_template("omne.html")

@app.route("/clanky")
def clanky():
    return render_template("clanky.html", clanky=Clanky)

@app.route("/clanek/<string:id>/")
def clanek(id):
    return render_template("clanek.html", id=id)

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

@app.route("/atheny")
def atheny():
    return render_template("atheny.html")

@app.route("/process_mail", methods=["POST","GET"])
def process_mail():
    jmeno=request.form["jmeno"]
    prijmeni=request.form["prijmeni"]
    email=request.form["email"]
    predmet=request.form["predmet"]
    zprava=request.form["zprava"]
    msg = Message("Test", sender='zacpalweb@gmail.com', recipients=['zacpalweb@email.com'])
    msg.body(jmeno, prijmeni, email, predmet, zprava)
    mail.send(msg)

    return flash("Děkuji za dotaz, odpovím hned jak to bude možné.")

"""
@app.route("/login/", methods=['GET'])
def login():
    return render_template('login.html')
"""
@app.route("/napsat_clanek", methods=['GET'])
def login():
    return render_template('napsat_clanek.html')

@app.route("/login_post", methods=['POST'])
def login_post():
    login = request.form.get('login')
    password = request.form.get('password')
    if login=="admin" and password=="heslo":
        return render_template('napsat_clanek.html')
    else:
        return flash("Špatné přihlašovací údaje")
        return render_template('login.html')




if __name__ == "__main__":
    app.run(debug=True)
