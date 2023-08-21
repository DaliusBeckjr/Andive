from flask import Flask, session
from flask_bcrypt import Bcrypt 
from flask_cors import CORS


app = Flask(__name__)
Bcrypt = Bcrypt(app)

# r"/*" -> which is the route will be set to a specific origin
cors = CORS(app, resources={r"/*": {"origins": "*"}})
# we can also say ... 
# cors = CORS(app, resources={r"/*": {"origins": "*", "allow_headers": "Access-Control-Allow-Origin"}})

app.secret_key = "Cup of coffee in the Big Time."