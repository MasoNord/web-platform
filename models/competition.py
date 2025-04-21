from app import db

class Competition(db.Model):
    __tablename__ = 'competitions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    discipline = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    registration_end = db.Column(db.Date, nullable=False)
    format = db.Column(db.String(20), nullable=False)
    max_participants = db.Column(db.Integer)
    status = db.Column(db.String(20), default='draft')
    organizer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey('regions.id'))

    teams = db.relationship('Team', backref='competition', lazy=True)
    applications = db.relationship('Application', backref='competition', lazy=True)

    def __repr__(self):
        return f'<Competition {self.title}>'