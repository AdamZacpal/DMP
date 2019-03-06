# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask_mail import Mail, Message


from flask import Flask, render_template, request, url_for, flash, redirect, logging, session
from data import Clanky
#from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
app = Flask(__name__)

app.secret_key=b"rcKeEd5VAz3tKvpxVWf1ff5XrpsNZyeD"

app.config["MYSQL_DATABASE_HOST"]="localhost"
app.config["MYSQL_DATABASE_USER"]="root"
app.config["MYSQL_DATABASE_PASSWORD"]="heslo"
app.config["MYSQL_DATABASE_DB"]="myflaskapp"
app.config["MYSQL_DATABASE_CURSORCLASS"]="DictCursor"

#mysql = MySQL(app)
Clanky=Clanky()

app.config.update(dict(
    DEBUG=True,
    MAIL_SERVER = 'smtp.googlemail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'zacpalweb',
    MAIL_PASSWORD = 'Fotbal123.'
))
mail= Mail(app)

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

@app.route("/kontakt", methods=["POST","GET"])
def kontakt():
    return render_template("kontakt.html")

@app.route("/atheny")
def atheny():
    return render_template("atheny.html")

@app.route("/kontakt", methods=["POST","GET"])
def process_mail():
    jmeno=request.form["jmeno"]
    prijmeni=request.form["prijmeni"]
    email=request.form["email"]
    predmet=request.form["predmet"]
    zprava=request.form["zprava"]
    msg = Message("Test", sender='zacpalweb@gmail.com', recipients=['zacpalweb@email.com'])
    msg.body(jmeno, prijmeni, email, predmet, zprava)
    mail.send(msg)
    flash("Děkuji za dotaz, odpovím hned jak to bude možné.")


class RegisterForm(Form):
    jmeno = StringField('Jméno', [validators.Length(min=1, max=50)])
    prezdivka = StringField('Přezdívka', [validators.Length(min=1, max=25)])
    heslo = PasswordField('Heslo', [validators.DataRequired(), validators.EqualTo('potvrzeni', message='Hesla se neshodují')])
    potvrzeni = PasswordField('Potvrzení hesla')

@app.route("/registrace", methods=["GET","POST"])
def registrace():
    form = RegisterForm(request.form)
    if request.method=="POST" and form.validate():
        jmeno=form.jmeno.data
        prezdivka=form.prezdivka.data
        heslo=sha256_crypt.encrypt(str(form.heslo.data))

        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO users(jmeno, prezdivka, heslo) VALUES(%s, %s, %s,)",(jmeno, prezdivka, heslo))

        mysql.connection.commit()
        cur.close()

        flash("Právě jsi se registroval")
        return redirect(url_for("login"))
    return render_template("registrace.html", form=form)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        prezdivka=request.form["prezdivka"]
        heslo_candidate=request.form["heslo"]

        cur=mysql.connection.cursor()
        result=cur.execute("SELECT * FROM users WHERE prezdivka=%s",[prezdivka])
        if result>0:
            data=cur.fetchone()
            heslo=data["heslo"]

            if sha256_crypt.verify(heslo_candidate, heslo):
                app.logger.info("Hesla se shodují")
                session["loggen_in"]=True
                session["prezdivka"]=prezdivka
                flash("Právě jsi se přihlásil")
                return redirect(url_for("redakce"))
            else:
                error="Chybné přihlášení"
                return render_template("login.html", error=error)
            cur.close()
        else:
            error="Přezdívka nenalezena"
            return render_template("login.html", error=error)

    return render_template("login.html")

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("Tato stránka je pouze pro autory, přihlaste se prosím.")
            return redirect(url_for('login'))
    return wrap


@app.route("/logout")
def logout():
    session.clear()
    flash("Právě ses odhlásil")
    return redirect(url_for("login"))

@app.route("/redakce", methods=["GET","POST"])
@is_logged_in
def redakce():
    return render_template("redakce.html")







if __name__ == "__main__":
    app.run(debug=True)
