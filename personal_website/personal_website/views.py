"""
Routes and views for the flask application.
"""

import time
from flask import render_template
from personal_website import app

@app.route("/")
def home():
    return render_template(
        "index.html",
        title="主页",
        time=time.strftime("现在是%Y年，%m月%d日，你好！"),
        age=time.localtime().tm_year - 2008)
@app.route("/github")
def github():
    return render_template(
        "github.html",
        title="GitHub")
@app.route("/bilibili")
def bilibili():
    return render_template(
        "bilibili.html",
        title="Bilibili")
