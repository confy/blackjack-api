""" Application factory pattern for Flask """
from flask import Flask


def create_app():
    """ Creates the Flask app, with the API and web blueprints """
    app = Flask(__name__)
    from .api import bp_api
    from .web import bp_web
    app.register_blueprint(bp_api, url_prefix="/api")
    app.register_blueprint(bp_web, url_prefix="/")
    return app
