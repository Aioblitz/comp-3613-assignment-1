from App.database import db
from enum import Enum

class Application(db.Model):
    application_id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    status = db.Column(db.Enum('pending', 'accepted', 'rejected', name='application_status'), default='pending', nullable=False)

    def __init__(self, job_id, student_id, status='pending'):
        self.job_id = job_id
        self.student_id = student_id
        self.status = status

