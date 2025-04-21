from app import db

class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    captain_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    competition_id = db.Column(db.Integer, db.ForeignKey('competitions.id'), nullable=False)
    status = db.Column(db.String(20), default='forming')

    members = db.relationship('TeamMember', backref='team', lazy=True, cascade='all, delete-orphan')
    applications = db.relationship('Application', backref='team', lazy=True)

    def __repr__(self):
        return f'<Team {self.name}>'