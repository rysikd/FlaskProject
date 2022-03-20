from flask import Flask

app = Flask(__name__)

from FlaskProject import db

db.create_db_for_books()
