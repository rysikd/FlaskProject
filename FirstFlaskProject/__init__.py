from flask import Flask

app = Flask(__name__)
from . import main_flask

from . import db
db.create_db_for_books()
