from flask import Flask
app = Flask(__name__)

app.secret_key = "mybookshelf"
from flask_bcrypt import Bcrypt
BCRYPT = Bcrypt(app)
DATABASE = ""

# ADD SCHEMA FROM SQL WORKBEND INTO DATABASE