from app import *
from flask import render_template
from .form import LoginForm


@app.route("/")
def index():
    return render_template('index.html', title="Главная")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print("OK")
    return render_template('login.html', title="Авторизация с помощью Custom forms")


@app.route("/login_quick_form", methods=["GET", "POST"])
def login_quick_form():
    form = LoginForm()

    if form.validate_on_submit():
        print("QuickForm - is ok")
    return render_template('login_quick_form.html', form=form, title="Авторизация с помощью Quick_form()")


@app.route('/login_custom_wtforms', methods=["POST", "GET"])
def login_custom_wtforms():
    form = LoginForm()
    if form.validate_on_submit():
        print("Custom WTForms - is ok")
    return render_template('login_custom_wtforms.html', form=form, title="Авторизация с помощью Custom WTForms")
