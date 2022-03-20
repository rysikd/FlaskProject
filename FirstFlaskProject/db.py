import sqlite3
from FirstFlaskProject.settings import DATABASE


def create_db_for_books():
    con = sqlite3.connect(DATABASE)