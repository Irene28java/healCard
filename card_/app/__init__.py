import os
from flask import Flask
from .models import db

def create_app():
    app = Flask(__name__)

    # Configuración base
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdb.db'
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'clave_secreta_segura'

    # Si tienes una clase de configuración en config.py, descomenta esta línea:
    # app.config.from_object('config.Config')

    # Inicializar extensiones
    db.init_app(app)

    # Registrar blueprints
    from .routes import bp
    app.register_blueprint(bp)

    # Crear tablas si no existen
    with app.app_context():
        from . import models  # Necesario para que detecte los modelos
        db.create_all()

    return app
