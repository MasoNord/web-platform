from datetime import datetime
from models import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # admin, regional, athlete
    region_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    competitions_organized = db.relationship('Competition', backref='organizer', lazy=True)
    teams = db.relationship('TeamMember', backref='member', lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)