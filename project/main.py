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


@main.route('/lectures')
@login_required
def lectures():
    q = request.args.get('q')
    if q:
        lectures = models.Lecture.query.filter(models.Lecture.tag.contains(f'{q}'))
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


@main.route('/lecture/<int:id>', methods=['GET', 'POST'])
@login_required
def lecture(id):
    lecture = models.Lecture.query.filter_by(id=id)
    if request.method == 'GET':

        return render_template('lecture.html', data=lecture)
    else:
        setattr(current_user, 'completed_lectures', current_user.completed_lectures + lecture.name)
        db.session.commit()


@main.route('/create_lectures', methods=['GET', 'POST'])
@login_required
def create_lectures():
    if current_user.grade == 4:
        if request.method == 'POST':
            text = request.form.get('text')
            name = request.form.get('name')
            result = models.Lecture(
                text=text,
                name=name,
            )
            db.session.add(result)
            db.session.commit()
            return redirect(f'/lecture/{id}')

        else:
            return render_template('create_lectures.html')
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
    user = current_user
    if request.method == 'GET':
        render_template(
            'statistic.html',
            data=current_user.completed_lectures,
            data2=current_user.completed_tests
        )
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

