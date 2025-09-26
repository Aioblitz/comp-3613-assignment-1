from .User import User
from App.database import db

class Employer(User):
    orgName = db.Column(db.String(150), nullable=False)
    pass