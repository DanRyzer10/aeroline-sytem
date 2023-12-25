from flask import Blueprint, render_template, request
from flask import flash, redirect, url_for
from utils.db import db
from flask_login import login_user, logout_user, login_required
import bcrypt
from auth.loginform import LoginForm

auth = Blueprint("auth", __name__, url_prefix="/auth")

@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        user = db.users.find_one({"username": username})
        if user is None:
            flash('El usuario no existe', 'danger')
            return render_template('views/auth/login.html')
        if verify_password(password, user['password']):
            login_user(user)
            flash('Bienvenido {}'.format(user['username']), 'success')
            return redirect(url_for('index', username=user['username']))
        else:
            flash('La contraseña es incorrecta', 'danger')
            return render_template('views/auth/login.html')
        
        
    return render_template('views/auth/login.html', form=form)
        
   


def verify_password(password, password_hash):
    return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))




