from flask_login import UserMixin

from . import db


class Intern(UserMixin, db.Model):
    """Стажер"""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    grade = 1
    cources = db.Column(db.String(100))
    lectures =  db.Column(db.String(100))


class Barista(UserMixin, db.Model):
    """Бариста"""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    grade = 1
    cources = db.Column(db.String(100))
    lectures = db.Column(db.String(100))


class Manager(UserMixin, db.Model):
    """Менеджер"""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    grade = 2
    cources = db.Column(db.String(100))
    lectures = db.Column(db.String(100))


class Administrator(UserMixin, db.Model):
    """Управляющий"""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    grade = 3
    cources = db.Column(db.String(100))
    lectures = db.Column(db.String(100))


class Hr_manager(UserMixin, db.Model):
    """Менеджер по персоналу"""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    grade = 4


class Lecture(UserMixin, db.Model):
    """Лекция"""

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(5000), nullable=False)


class Course(UserMixin, db.Model):
    """Курс"""

    id = db.Column(db.Integer, primary_key=True)
    lectures = db.relationship('Lecture', backref='cource')

