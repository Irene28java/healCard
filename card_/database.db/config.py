import os 

class Config:
    SECRET_KEY = "clave-ultra-segura-calei"
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False