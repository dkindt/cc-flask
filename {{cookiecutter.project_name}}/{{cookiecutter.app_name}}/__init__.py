import os

from flask import Flask


def create_app(init_config=None):
    """ Create and configure a Flask application.
    """
    app = Flask(__name__, instance_relative_config=True)



    return app
