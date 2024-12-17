from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)    
    app.config.from_object(Config) # Carga configuraciones desde el archivo config.py

    # Importa y registra los blueprints
    from app.controllers.main_controller import main

    app.register_blueprint(main) # Rutas principales

    return app

