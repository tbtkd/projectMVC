from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = 'tu_clave_secreta_aqui'  # Asegúrate de cambiar esto en producción

    from app.controllers.main_controller import main

    app.register_blueprint(main)

    return app

