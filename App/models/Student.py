from .user import User
from App.database import db

class Student(User):
    __tablename__ = 'student'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'student',
    }

    def __init__(self, username, password, firstName, lastName):
        super().__init__(username, password)
        self.firstName = firstName
        self.lastName = lastName

    def __repr__(self):
        return f'<Student {self.firstName} {self.lastName}>'