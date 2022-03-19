from flask import render_template
from FirstFlaskProject import app

from .settings import DATABASE

# app = Flask(__name__)

@app.route("/")
def hello_world():
    book = {
        "title": "鬼滅の刃",
        "price": "1yen",
        "arrival_date": "today",
    }
    return render_template(
        "index.html",
        book=book
    )
