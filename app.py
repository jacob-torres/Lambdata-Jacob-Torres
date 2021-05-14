from flask import Flask, render_template
from flask_sqlalchemy import sqlalchemy

App = Flask(__name__)

@App.route('/')
def root():
