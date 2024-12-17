from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.controllers.main_controller import main

    app.register_blueprint(main)

    return app

