from flask_login import UserMixin

from . import db


class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    completed_lectures = db.Column(db.String(100), nullable=True)
    completed_tests = db.Column(db.String(100), nullable=True)
    grade = db.Column(db.Integer(), nullable=False)


# class Intern(UserMixin, db.Model):
#     """Стажер"""
#
#     grade = 0
#     cources = db.Column(db.String(100))
#     lectures =  db.Column(db.String(100))
#     completed_tests =  db.Column(db.String(100))
#
#
# class Barista(UserMixin, db.Model):
#     """Бариста"""
#
#     grade = 1
#     cources = db.Column(db.String(100))
#     lectures = db.Column(db.String(100))
#     completed_tests = db.Column(db.String(100))
#
#
# class Manager(UserMixin, db.Model):
#     """Менеджер"""
#
#     grade = 2
#     cources = db.Column(db.String(100))
#     lectures = db.Column(db.String(100))
#     completed_tests = db.Column(db.String(100))
#
#
# class Administrator(UserMixin, db.Model):
#     """Управляющий"""
#
#     grade = 3
#     cources = db.Column(db.String(100))
#     lectures = db.Column(db.String(100))
#     completed_tests = db.Column(db.String(100))
#
#
# class Hr_manager(UserMixin, db.Model):
#     """Менеджер по персоналу"""
#     grade = 4


class Lecture(UserMixin, db.Model):
    """Лекция"""

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(5000), nullable=False)
    name = db.Column(db.String(5000), nullable=False)


class Course(UserMixin, db.Model):
    """Курс"""

    id = db.Column(db.Integer, primary_key=True)
    lectures = db.Column(db.Integer(),  db.ForeignKey("lecture.id"))
    name = db.Column(db.String(5000), nullable=False)


class Test(UserMixin, db.Model):
    """Тест"""

    id = db.Column(db.Integer, primary_key=True)
    lecture = db.Column(db.Integer(),  db.ForeignKey("lecture.id"))
    name = db.Column(db.String(5000), nullable=False)
