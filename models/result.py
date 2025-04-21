from app import db

class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    competition_id = db.Column(db.Integer, db.ForeignKey('competitions.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    position = db.Column(db.Integer)
    score = db.Column(db.Integer)

    __table_args__ = (
        db.UniqueConstraint('competition_id', 'team_id', name='_competition_team_uc'),
    )

    def __repr__(self):
        return f'<Result {self.position} place in Competition {self.competition_id}>'