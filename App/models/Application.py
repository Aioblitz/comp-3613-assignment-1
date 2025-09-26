from App.database import db
from enum import Enum

class Application(db.Model):
    application_id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    status = db.Column(db.Enum('pending', 'accepted', 'rejected', name='application_status'), default='pending', nullable=False)

    job = db.relationship('Job', backref=db.backref('applications', lazy=True))
    student = db.relationship('Student', backref=db.backref('applications', lazy=True))

    def __init__(self, job_id, student_id, status='pending'):
        self.job_id = job_id
        self.student_id = student_id
        self.status = status

    def __repr__(self):
        job_title = self.job.title if self.job else 'Unknown'
        student_name = f'{self.student.firstName} {self.student.lastName}' if self.student and hasattr(self.student, 'firstName') and hasattr(self.student, 'lastName') else 'Unknown'
        return f'<Application {self.application_id} - Job {self.job_id} "{job_title}" - Student {self.student_id} "{student_name}" : Application status "{self.status}">'
