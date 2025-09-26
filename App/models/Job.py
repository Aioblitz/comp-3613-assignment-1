from App.database import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employer_id = db.Column(db.Integer, db.ForeignKey('employer.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    employer = db.relationship('Employer', backref=db.backref('job', lazy=True))
    
    def __init__(self, title, description, employer_id):
        self.title = title
        self.description = description
        self.employer_id = employer_id

    def get_json(self):
        return {
            'id': self.id,
            'employer_id': self.employer_id,
            'title': self.title,
            'description': self.description
        }
    def __repr__(self):
        org_name = self.employer.orgName if self.employer and hasattr(self.employer, 'orgName') else 'Unknown'
        return f'<Job {self.id} {self.title} - Employer {self.employer_id} {org_name} : "{self.description}">'