from flask import Flask, render_template, request, redirect, flash, jsonify
from markupsafe import escape
import math
from flask import url_for
from flask import make_response
import hashlib
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template('login.html')

@app.route("/registro_usuario", methods=["GET", "POST"])
def registro_usuario():
    return render_template('registro.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)