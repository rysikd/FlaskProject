from flask import render_template
#from FlaskProject import app
from flask import Flask

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5555, threaded=True)