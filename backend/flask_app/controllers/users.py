from flask_app import app, Bcrypt
from flask import render_template, session, request, jsonify

# get methods are by default

@app.route('/', methods = ['GET'])
def index():
    return ('hello world!')

# register route
@app.route('/register', methods = ['POST'])
def register():
    pass

#login route
@app.route('/login', methods = ['POST'])
def login():
    pass







# made two ways, two examples to get information
# from the backend through fetch api and axios
# these examples will not stay for long but will be moved
# into code snippets or even part of my blog on medium ( feel free to follow me )
# @app.route('/shark', methods = ['GET'])
# def shark():
#     return ('shark!')


# @app.route('/ping', methods = ['GET'])
# def ping():
#     return jsonify('ping!')



