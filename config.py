import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://flask_user:password123@localhost/FSP')
    SQLALCHEMY_TRACK_MODIFICATIONS = False