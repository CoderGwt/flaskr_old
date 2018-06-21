# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route("/")
# def index():
#     return "Hello world"
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
# TODO all the imports
import os
import sqlite3
from flask import Flask, request, url_for, session, g, redirect, abort, render_template, flash

app = Flask(__name__)  # create the application instance
app.config.from_object(__name__)  # load config from this file, flaskr.py

# load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, "flaskr.db"),
    ECRET_KEY='this is the secret key',
    USERNAME='admin',
    PASSWORD='admin'
))
app.config.from_envvar("FLASK_SETTINGS", silent=True)


def connect_db():
    """connects to the specific databases"""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


if __name__ == '__main__':
    app.run(debug=True)


