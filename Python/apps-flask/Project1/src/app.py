from flask import Flask

from src.ext import config


def create_app():
    """Factory to create a Flask app based on factory pattern."""

    app = Flask(__name__)
    config.init_app(app)

    return app
