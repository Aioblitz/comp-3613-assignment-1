import click, pytest, sys
from sqlalchemy.orm import with_polymorphic
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, Student, Staff, Employer, Job, Application
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    jimbo = Student(username='jimbo', password='jimbopass', firstName='Jimbo', lastName='Jenkins')
    nami = Student(username='nami', password='namipass', firstName='Nami', lastName='Leon')
    steve = Staff(username='steve', password='stevepass')
    grolnok = Employer(username='grolnok', password='grolnokpass', orgName='Grolnok Inc.')
    tsa = Job(title='TSA', description='Technical Systems Analyst', employer_id=4)
    jimShortList = Application(job_id=1, student_id=2)
    db.session.add_all([jimbo, nami, steve, grolnok,tsa,jimShortList])
    db.session.commit()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups
staff_cli = AppGroup('staff', help='Staff object commands')

#staff adds a student to a job's shortlist
@staff_cli.command("shortlist", help="Shortlist a student for a job")
def shortlist_student_command():
    #lists jobs
    jobs = db.session.scalars(db.select(Job)).all()
    for job in jobs:
         print(job)
    job_id = click.prompt("Enter the job ID to shortlist a student for", type=int)
    #lists students who are not yet shortlisted for the job
    not_shortlisted = db.select(Application.student_id).filter_by(job_id=job_id)
    students = db.session.scalars(db.select(Student).filter(~Student.id.in_(not_shortlisted))).all()
    if not students:
        print(f'All students are already shortlisted for job ID {job_id}')
        return
    print(f'Students not yet shortlisted for job ID {job_id}:')
    for student in students:
        print(student)
    #Choose student to shortlist
    student_id = click.prompt("Enter the student ID to shortlist", type=int)
    new_application = Application(job_id=job_id, student_id=student_id)
    db.session.add(new_application)
    db.session.commit()
    print(f'Student ID {student_id} shortlisted for job ID {job_id}')




app.cli.add_command(staff_cli)

student_cli = AppGroup('student', help='Student object commands') 

@student_cli.command("list", help="Lists shortlisted positions for student")
def list_student_shortlist_command():
    students = db.session.scalars(db.select(Student)).all()
    for student in students:
        print(student)
    student_id = click.prompt("Enter your student ID to view your shortlisted positions", type=int)
    applications = db.session.scalars(db.select(Application).filter_by(student_id=student_id)).all()
    if not applications:
        print(f'No shortlisted positions found for student ID {student_id}')
        return
    print(f'Shortlisted positions for student ID {student_id}:')
    for application in applications:
        print(application)
    
app.cli.add_command(student_cli)

employer_cli = AppGroup('employer', help='Employer object commands')  

@employer_cli.command("change-status", help="Change application status")
def change_application_status():
    #lists jobs
    jobs = db.session.scalars(db.select(Job)).all()
    for job in jobs:
        print(job)
    job_id = click.prompt("Enter the job ID", type=int)
    #lists applications for the job
    applications = db.session.scalars(db.select(Application).filter_by(job_id=job_id)).all()
    if not applications:
        print(f'No applications found for job ID {job_id}')
        return
    print(f'Applications for job ID {job_id}:')
    for application in applications:
        print(application)
    #Choose application to change status
    student_id = click.prompt("Enter the student ID to change status for", type=int)
    application = db.session.scalars(db.select(Application).filter_by(job_id=job_id, student_id=student_id)).first()
    if not application:
        print(f'No application found for student ID {student_id} and job ID {job_id}')
        return
    #Change status
    new_status = click.prompt("Enter the new status", type=click.Choice(['accepted', 'rejected']))

    application.status = new_status
    db.session.commit()
    print(f'Application status updated to "{new_status}" for student ID {student_id} and job ID {job_id}')

@employer_cli.command("create", help="Create a new job posting")
def create_job_command():
    employers = db.session.scalars(db.select(Employer)).all()
    for employer in employers:
        print(employer)

    employer_id = click.prompt("Enter your employer ID", type=int)
    title = click.prompt("Enter the job title", type=str)
    description = click.prompt("Enter the job description", type=str)
    new_job = Job(title=title, description=description, employer_id=employer_id)
    db.session.add(new_job)
    db.session.commit()
    print(f'Job "{title}" created with ID {new_job.id} for employer ID {employer_id}')
    
    

app.cli.add_command(employer_cli)

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

#I want to list all user types in the db
@user_cli.command("list", help="Lists users in the database")
def list_user_command():
    UserPoly = with_polymorphic(User, [Student, Staff, Employer])
    users = db.session.scalars(db.select(UserPoly)).all()
    for user in users:
        print(user)

# Command to list all jobs
@user_cli.command("list-jobs", help="Lists jobs in the database")
def list_jobs_command():
    jobs = db.session.scalars(db.select(Job)).all()
    for job in jobs:
        print(job)


app.cli.add_command(user_cli) # add the group to the cli





































'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)