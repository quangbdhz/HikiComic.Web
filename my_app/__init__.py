from flask import Flask, request, render_template, app
from flask_babelex import Babel
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import pyodbc

app = Flask(__name__)
# EC2 ubuntu
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://admin:quang810@hikicomic.cctxaxqlrtny.us-east-1.rds.amazonaws.com:1433/HikiComic?driver=ODBC+Driver+17+for+SQL+Server'
# Windows
# app.config[
#     'SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://admin:quang810@hikicomic.cctxaxqlrtny.us-east-1.rds.amazonaws.com:1433/HikiComic?driver=SQL+Server'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=120)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = '1fabace46bcf5b6eebda3de7'

db = SQLAlchemy(app=app)

from my_app import routes

babel = Babel(app=app)


@babel.localeselector
def get_locale():
    return 'vi'
