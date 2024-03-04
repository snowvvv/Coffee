from flask_login import UserMixin

from . import db


class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    completed_lectures = db.Column(db.String(100), nullable=False)
    completed_tests = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.Integer(), nullable=False)


# class Intern(UserMixin, db.Model, User):
#     """Стажер"""
#
#     grade = 1
#     cources = db.Column(db.String(100))
#     lectures =  db.Column(db.String(100))
#
#
# class Barista(UserMixin, db.Model, User):
#     """Бариста"""
#
#     grade = 1
#     cources = db.Column(db.String(100))
#     lectures = db.Column(db.String(100))
#
#
# class Manager(UserMixin, db.Model, User):
#     """Менеджер"""
#
#     grade = 2
#     cources = db.Column(db.String(100))
#     lectures = db.Column(db.String(100))
#
#
# class Administrator(UserMixin, db.Model, User):
#     """Управляющий"""
#
#     grade = 3
#     cources = db.Column(db.String(100))
#     lectures = db.Column(db.String(100))
#
#
# class Hr_manager(UserMixin, db.Model, User):
#     """Менеджер по персоналу"""
#
#     grade = 4


class Lecture(UserMixin, db.Model):
    """Лекция"""

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(5000), nullable=False)
    cource = db.relationship('Course', backref='lecture')
    name = db.Column(db.String(5000), nullable=False)


class Course(UserMixin, db.Model):
    """Курс"""

    id = db.Column(db.Integer, primary_key=True)
    lectures = db.relationship('Lecture', backref='cource')
    name =  db.Column(db.String(5000), nullable=False)


class Test(UserMixin, db.Model):
    """Тест"""

    id = db.Column(db.Integer, primary_key=True)
    cource = db.relationship('Course', backref='test')
    name = db.Column(db.String(5000), nullable=False)
