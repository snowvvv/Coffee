import os
import configparser

import smtplib
from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект
from email.mime.text import MIMEText

from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from . import db
import models
from . import ALLOWED_EXTENSIONS

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('new_index.html')


@main.route('/courses')
@login_required
def courses():
    q = request.args.get('q')
    if q:
        course = models.Course.query.filter(models.Course.tag.contains(f'{q}'))
    else:
        course = models.Course.query.all()
    return render_template('new_search_teammates.html', data=course)


@main.route('/courses/<int:id>', methods=['GET', 'POST'])
@login_required
def cources_lectures():
    course = models.Course.query.filter_by(id=id)
    lectures = course.lectures

    if request.method == 'POST':
        return redirect(f'/lecture/{id}')

    else:
        return render_template('new_search_teammates.html', data=lectures)


@main.route('/lecture/<int:id>', methods=['GET'])
@login_required
def activity_pet(id):
    lecture = models.Lecture.query.filter_by(id=id)
    return render_template('new_search_teammates.html', data=lecture)


@main.route('/create_lecture', methods=['GET', 'POST'])
@login_required
def create_lecture():
    if current_user.grade == 4:
        if request.method == 'POST':
            text = request.form.get('text')
            course = request.form.get('course')
            name = request.form.get('name')
            result = models.Lecture(
                text=text,
                course=course,
                name=name,
            )
            db.session.add(result)
            db.session.commit()
            return redirect(f'/lecture/{id}')

        else:
            render_template('new_search_teammates.html')


@main.route('/create_cource', methods=['GET', 'POST'])
@login_required
def create_lecture():
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
            render_template('new_search_teammates.html')
