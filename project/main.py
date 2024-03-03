import os
import configparser

import smtplib
from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект
from email.mime.text import MIMEText

from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from . import db
from .models import User, Pets, Health, Activity, Food, Vets, Consultation, Povedenie, Freetime
from . import UPLOAD_FOLDER_PETS,UPLOAD_FOLDER_VETS, ALLOWED_EXTENSIONS

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('new_index.html')
