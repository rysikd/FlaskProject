from flask import Flask

app = Flask(__name__)
from FirstFlaskProject import main_flask

from FirstFlaskProject import db
db.create_db_for_books()
