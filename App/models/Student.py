from .User import User
from App.database import db

class Student(User):
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    pass