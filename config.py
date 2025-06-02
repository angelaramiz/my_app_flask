# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'tu_clave_secreta_aqui'
    # Configuración de PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:22122000@localhost/mi_flask_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
