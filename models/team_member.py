from app import db

class TeamMember(db.Model):
    __tablename__ = 'team_members'

    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    role = db.Column(db.String(50))

    user = db.relationship('User', backref='team_memberships')

    def __repr__(self):
        return f'<TeamMember {self.user_id} in Team {self.team_id}>'