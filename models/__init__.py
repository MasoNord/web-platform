from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .region import Region
from .competition import Competition
from .team import Team
from .team_member import TeamMember
from .application import Application
from .result import Result