from app import db

class Region(db.Model):
    __tablename__ = 'regions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    users = db.relationship('User', backref='region', lazy=True)
    competitions = db.relationship('Competition', backref='region', lazy=True)

    def __repr__(self):
        return f'<Region {self.name}>'
