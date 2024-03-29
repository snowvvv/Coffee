from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('new_login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # Хэширование пароля и сравнение с хэшированным паролем из дб
    if not user or not check_password_hash(user.password, password) or email is None or password is None:
        flash('Пожалуйста проверьте введенные данные и попробуйте снова')
        return redirect(url_for('auth.login'))  # Если юзера нет или пароль неверный - перезагрузка страницы

    # Если проверка проходит, значит введенные данные верны
    login_user(user, remember=True)
    return redirect(url_for('main.index'))


@auth.route('/signup', methods=['GET'])
def signup():
    return render_template('new_signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    phone = request.form.get('phone')
    password = request.form.get('password')
    name = request.form.get('name')
    role = request.form.get('role')

    user = User.query.filter_by(email=email).first()  # Если это возвращает юзера, то значит маил уже есть в базе
    new_user = None
    if user:  # если такой юзер уже есть, надо сделать редирект на регистрацию, чтобы пользователь мог попробовать снова
        flash('Email уже используется')
        return redirect(url_for('auth.signup'))
    if len(email) < 1 or len(password) < 1 or len(name) < 1:
        flash('Пожалуйста заполните все поля')
        return redirect(url_for('auth.signup'))
    if role == 'Intern':
        new_user = Intern(
            email=email,
            phone=phone,
            password=generate_password_hash(password, method='sha256'),
            name=name
        )
    elif role == 'Barista':
        new_user = Barista(
            email=email,
            phone=phone,
            password=generate_password_hash(password, method='sha256'),
            name=name
        )

    elif role == 'Manager':
        new_user = Manager(
            email=email,
            phone=phone,
            password=generate_password_hash(password, method='sha256'),
            name=name
        )

    elif role == 'Administrator':
        new_user = Barista(
            email=email,
            phone=phone,
            password=generate_password_hash(password, method='sha256'),
            name=name
        )

    elif role == 'Hr_manager':
        new_user = Hr_manager(
            email=email,
            phone=phone,
            password=generate_password_hash(password, method='sha256'),
            name=name
        )

    # добавление пользователя в базу
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
