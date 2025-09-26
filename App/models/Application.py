from App.database import db
from enum import Enum

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    status = db.Column(db.Enum('pending', 'accepted', 'rejected', name='application_status'), default='pending', nullable=False)

    def __init__(self, job_id, status='pending'):
        self.job_id = job_id
        self.status = status

    def get_json(self):
        return {
            'id': self.id,
            'job_id': self.job_id,
            'status': self.status
        }