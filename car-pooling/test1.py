from flask import Flask
app = Flask(__name__)



# EVERYTHING get all and get by ids
# create commute
# update commute
# delete commute
# get commute

# create user
# update user
# delete user?
# get user
# Score of user increases by two and decreases by one for each drive it is
# in(including its own commute)

# tests

@app.route("/")
def hello():
    return "Start page"


@app.route("/commute")
def create_commute():
    return "Create commute!"  # post


@app.route("/person")
def get_score():
    return "Get Score!"  # get all score




# change score (increase by one or decrase by one)


# Create a commute - creat. (read from jwt) is the driver, and spec. passangers


# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
# https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way


# flask --> pytest --> database alchemy --> make public api

# auto deploy (docker, kubernetes)
# connects api to react
# loging server (make api endpoints private)
