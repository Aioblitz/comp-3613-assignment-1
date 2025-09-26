from .user import User
from App.database import db

class Staff(User):
    __tablename__ = 'staff'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity': 'staff'}
    
    def __init__(self, username, password):
        super().__init__(username, password)

    def __repr__(self):
        return f'<Staff {self.username}>'