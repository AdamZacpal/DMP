# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Importy nezbytných modulů
from flask_mail import Mail, Message
from flask import Flask, render_template, request, url_for, flash, redirect, logging, session
from flaskext.mysql import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from config import MailConfig, MySQLConfig, KeyConfig, regklic
app = Flask(__name__)

# Nastavení MySQL
mysql = MySQL()
app.config.from_object(KeyConfig)
app.config.from_object(MySQLConfig)
mysql.init_app(app)

# Nastavení Mailu
app.config.from_object(MailConfig)
mail= Mail(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/omne")
def omne():
    return render_template("omne.html")

# Vytvoření náhledu článků
@app.route("/clanky")
def clanky():
    # Výběr všech článků z databáze
    cur=mysql.get_db().cursor()
    result=cur.execute("SELECT * FROM clanky")
    clanky=cur.fetchall()
    if result>0:
        return render_template("clanky.html", clanky=clanky)
    else:
        msg="Žádné články"
        return render_template("clanky.html", msg=msg)
    cur.close()

# Vytvoření článku
@app.route("/clanek/<string:id>/")
def clanek(id):
    # Výběr jednotlivých článků z databáze
    cur=mysql.get_db().cursor()
    result=cur.execute("SELECT * FROM clanky WHERE id=%s",[id])
    clanek=cur.fetchone()
    return render_template("clanek.html", clanek=clanek)

@app.route("/kontakt", methods=["GET"])
def kontakt():
    return render_template("kontakt.html")

@app.route("/atheny")
def atheny():
    return render_template("atheny.html")

# Kontakt
@app.route("/kontakt", methods=["POST"])
def process_mail():
    # Vytáhnutí údajů formuláře
    jmeno=request.form["jmeno"]
    prijmeni=request.form["prijmeni"]
    email=request.form["email"]
    predmet=request.form["predmet"]
    zprava=request.form["zprava"]

    # Vytvoření a odeslání samotné zprávy
    msg = Message("Dotaz z webu" , sender='zacpalweb@gmail.com', recipients=['zacpalweb@gmail.com'])
    mail_body=jmeno+" "+prijmeni+"\n"+email+"\n"+predmet+"\n"+zprava
    msg.body = mail_body
    mail.send(msg)
    flash("Děkuji za dotaz, odpovím hned jak to bude možné.")
    return redirect(url_for("kontakt"))

# Formulář pro registraci
class RegisterForm(Form):
    jmeno = StringField('Jméno', [validators.Length(min=1, max=50)])
    prezdivka = StringField('Přezdívka', [validators.Length(min=1, max=25)])
    heslo = PasswordField('Heslo', [validators.DataRequired(), validators.EqualTo('potvrzeni', message='Hesla se neshodují')])
    potvrzeni = PasswordField('Potvrzení hesla')
    klic = PasswordField('Ověřovací klíč')

# Registrace
@app.route("/registrace", methods=["GET","POST"])
def registrace():
    form = RegisterForm(request.form)
    # Validace
    if request.method=="POST" and form.validate():
        # Vytáhnutí údajů z formuláře
        jmeno=form.jmeno.data
        prezdivka=form.prezdivka.data
        heslo=sha256_crypt.encrypt(str(form.heslo.data))
        klic=form.klic.data
        # Potvrzení, že se jedná o člověka s registračním klíčem
        if klic==regklic:
            # Zápis údajů do databáze
            cur=mysql.get_db().cursor()
            cur.execute("INSERT INTO users(jmeno, prezdivka, heslo) VALUES(%s, %s, %s)",[jmeno, prezdivka, heslo])
            mysql.get_db().commit()
            cur.close()

            flash("Právě jsi se registroval")
            return redirect(url_for("login"))
        else:
            flash("Nemáte oprávnění k registraci")
            return render_template("index.html")

    return render_template("registrace.html", form=form)


# Přihlášení
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        # Vytáhnutí údajů z formuláře
        prezdivka=request.form["prezdivka"]
        heslo_candidate=request.form["heslo"]
        # Výběr uživatele z databáze
        cur=mysql.get_db().cursor()
        result=cur.execute("SELECT * FROM users WHERE prezdivka=%s",[prezdivka])
        if result>0:
            # Ověření údajů z formuláře a z databáze
            data=cur.fetchone()
            heslo=data[3]
            if sha256_crypt.verify(heslo_candidate, heslo):
                app.logger.info("Hesla se shodují")
                # Přihlášení
                session["logged_in"]=True
                session["prezdivka"]=prezdivka
                flash("Právě jsi se přihlásil")
                return redirect(url_for("redakce"))
            else:
                flash("Špatné heslo")
                return render_template("login.html")
            cur.close()
        else:
            flash("Přezdívka nenalezena")
            return render_template("login.html")

    return render_template("login.html")

# Kontrola přihlášení
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("Tato stránka je pouze pro autory, přihlaste se prosím.")
            return redirect(url_for('login'))
    return wrap

# Odhlášení
@app.route("/logout")
@is_logged_in
def logout():
    session.clear()
    flash("Právě ses odhlásil")
    return redirect(url_for("login"))


# Redakční systém
@app.route("/redakce", methods=["GET","POST"])
@is_logged_in
def redakce():
    # Výběr článků z databáze
    cur=mysql.get_db().cursor()
    result=cur.execute("SELECT * FROM clanky")
    clanky=cur.fetchall()
    if result>0:
        return render_template("redakce.html", clanky=clanky)
    else:
        msg="Žádné články"
        return render_template("redakce.html", msg=msg)
    cur.close()

# Formulář pro článek
class ClanekForm(Form):
    nazev = StringField('Název', [validators.Length(min=1, max=150)])
    body = TextAreaField('Text', [validators.Length(min=50)])
    autor = StringField('Autor', [validators.Length(min=1, max=150)])

# Přidávání článků
@app.route("/pridat_clanek", methods=["GET","POST"])
@is_logged_in
def pridat_clanek():
    form = ClanekForm(request.form)
    if request.method=="POST" and form.validate():
        # Vytáhnutí údajů z formuláře
        nazev=form.nazev.data
        body=form.body.data
        autor=form.autor.data
        # Zápis údajů do databáze
        cur=mysql.get_db().cursor()
        cur.execute("INSERT INTO clanky(nazev, body, autor) VALUES(%s, %s, %s)",[nazev, body, autor])
        mysql.get_db().commit()
        cur.close()
        flash("Článek vytvořen")
        return redirect(url_for("redakce"))
    return render_template("pridat_clanek.html", form=form)

# Upravení článků
@app.route("/upravit_clanek/<string:id>", methods=["GET","POST"])
@is_logged_in
def upravit_clanek(id):
    # Výběr jednotlivých článků z databáze
    cur=mysql.get_db().cursor()
    result=cur.execute("SELECT * FROM clanky WHERE id=%s", [id])
    clanek=cur.fetchone()
    form = ClanekForm(request.form)
    # Vložení dat z databáze do formuláře
    form.nazev.data=clanek[1]
    form.autor.data=clanek[2]
    form.body.data=clanek[3]

    if request.method=="POST" and form.validate():
        # Vytáhnutí údajů z formuláře
        nazev=request.form["nazev"]
        body=request.form["body"]
        autor=request.form["autor"]
        # Zápis údajů do databáze
        cur=mysql.get_db().cursor()
        cur.execute("UPDATE clanky SET nazev=%s, body=%s, autor=%s WHERE id=%s",[nazev, body, autor, id])
        mysql.get_db().commit()
        cur.close()
        flash("Článek aktualizován")
        return redirect(url_for("redakce"))
    return render_template("upravit_clanek.html", form=form)

# Vymazání článků
@app.route("/vymazat_clanek/<string:id>", methods=["POST"])
@is_logged_in
def vymazat_clanek(id):
    # Smazání jednotlivých článků z databáze
    cur=mysql.get_db().cursor()
    cur.execute("DELETE FROM clanky WHERE id=%s",[id])
    mysql.get_db().commit()
    cur.close()
    flash("Článek smazán")
    return redirect(url_for("redakce"))



if __name__ == "__main__":
    app.run(debug=True)
