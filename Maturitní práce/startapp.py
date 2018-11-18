# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/omne.html")
def omne():
    return render_template("omne.html")

@app.route("/clanky.html")
def clanky():
    return render_template("clanky.html")

@app.route("/kontakt.html")
def kontakt():
    return render_template("kontakt.html")




if __name__ == "__main__":
    app.run(debug=True)
