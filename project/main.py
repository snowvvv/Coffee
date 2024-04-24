import os
import configparser

import smtplib
from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект
from email.mime.text import MIMEText

from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from . import db
from . import models
from . import ALLOWED_EXTENSIONS

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
def profile():
    return render_template('profile.html')


@main.route('/lectures')
@login_required
def lectures():
    q = request.args.get('q')
    if q:
        lectures = models.Lecture.query.filter(models.Lecture.name.contains(f'{q}'))
    else:
        lectures = models.Lecture.query.all()
    return render_template('lectures.html', data=lectures)


@main.route('/courses/<int:id>', methods=['GET', 'POST'])
@login_required
def courses_lectures():
    course = models.Course.query.filter_by(id=id)
    lectures = course.lectures

    if request.method == 'POST':
        return redirect(f'/lecture/{id}')

    else:
        return render_template('courses_lectures.html', data=lectures)


@main.route('/lectures/<int:id>', methods=['GET', 'POST'])
@login_required
def lecture(id):
    lecture = models.Lecture.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('lecture.html', data=lecture)
    else:
        if current_user.completed_lectures:
            name = current_user.completed_lectures + ', ' + lecture.name
            setattr(current_user, 'completed_lectures', name)
            db.session.commit()
        else:
            setattr(current_user, 'completed_lectures', lecture.name)
            db.session.commit()
        return redirect('/lectures')


@main.route('/create_lecture', methods=['GET', 'POST'])
@login_required
def create_lecture():
    if current_user.grade == 4:
        if request.method == 'POST':
            name = request.form.get('name')
            text = request.form.get('text')
            result = models.Lecture(
                name=name,
                text=text,
            )
            db.session.add(result)
            db.session.commit()
            return redirect(f'/lectures')

        else:
            return render_template('create_lecture.html')
    else:
        return redirect(url_for('main.index'))


@main.route('/create_course', methods=['GET', 'POST'])
@login_required
def create_course():
    if current_user.grade == 4:
        if request.method == 'POST':
            name = request.form.get('name')
            result = models.Course(
                name=name
            )
            db.session.add(result)
            db.session.commit()
            return redirect(f'/courses')

        else:
            return render_template('create_course.html')


@main.route('/statistic', methods=['GET', 'POST'])
@login_required
def statistic():
    if request.method == 'GET':
        users = models.User.query.all()
        match current_user.grade:
            case 0:
                users = None
            case 1:
                users = None
            case 2:
                users = models.User.query.filter(models.User.grade < 2)
            case 3:
                users = models.User.query.filter(models.User.grade < 3)
            case 4:
                users = models.User.query.filter(models.User.grade < 4)
        return render_template('statistic.html', data1=current_user, data2=users)

    else:
        return redirect(f'/lalka_statistic/{id}')


@main.route('/lalka_statistic/<int:id>', methods=['POST'])
@login_required
def lalka_statistic():
    user = models.User.query.filter_by(id=id)
    return render_template(
        'lalka_statistic.html',
        data=user.completed_lectures,
        data2=user.completed_tests
    )

