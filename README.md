# Car-pooling-backend
Back office for keeping track of who has driven most among friends.

# To initialize
$ virtualenv venv -p python3
$ source venv/bin/activate
If no requirements.txt file exists:
$ pip-compile requirements.in
$ pip install -r requirements.txt
$ export FLASK_APP=car-pooling.py
$ flask run

# Dev commands
pip freeze > requirements.txt

## Python venv with right packages

flask-sqlalchemy

# BUG!!
Note sure

## Debug
# Upgrade pip
$ curl https://bootstrap.pypa.io/get-pip.py | python
$ pip install pip-tools
Need to install flask migrate in python2.7 :/ not sure why
$ pip2 install flask-migrate

# to run the application
$ chmod a+x app.py
$ ./app.py

# FLASK
# https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way

## Flask-Migrate
$ flask db init
$ flask db migrate -m "users table"
$ flask db upgrade
$ flask db downgrade

## Try out stuff in terminal (flash shell command runt python in python2)
from app import db
from app.models import User, Post


# tests --> make public --> marshmellow (lookup decorators)
# --> docker --> kubernetes --> React --> keycloak (login) --> change sqllite to postgress with postico?

*react handle redirects via file (dont want to hardcode endpoints, what happends if u wanna change these)
*do advanced git tutorial
*learn more ansible
*nginx?
*logs elk stack
