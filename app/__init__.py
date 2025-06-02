# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Inicializar SQLAlchemy con la aplicación
    db.init_app(app)
    
    # Importar y registrar blueprints
    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # Crear tablas al iniciar la aplicación
    with app.app_context():
        db.create_all()
    
    return app
