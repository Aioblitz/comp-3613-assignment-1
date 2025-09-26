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
    steve = Staff(username='steve', password='stevepass')
    grolnok = Employer(username='grolnok', password='grolnokpass', orgName='Grolnok Inc.')
    db.session.add_all([jimbo, steve, grolnok])
    db.session.commit()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups
staff_cli = AppGroup('staff', help='Staff object commands')
student_cli = AppGroup('student', help='Student object commands') 
employer_cli = AppGroup('employer', help='Employer object commands')  
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
    from sqlalchemy.orm import with_polymorphic
    UserPoly = with_polymorphic(User, [Student, Staff, Employer])
    users = db.session.scalars(db.select(UserPoly)).all()
    for user in users:
        print(user)


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