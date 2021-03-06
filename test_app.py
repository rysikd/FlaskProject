from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import abort
from settings import site

app = Flask(__name__)  # Flaskインスタンス作成

f_data = ['サイトポリシー', 'プライバシーポリシー', 'サイトマップ']


@app.route('/', methods=['GET', 'POST'])
def login_page():
    global f_data

    if request.method == 'GET':
        return render_template('index.html',
                               title=__name__,
                               message='test作成hp',
                               data=f_data)

    elif request.method == 'POST':
        content = request.form.get('form')
        return render_template('index.html',
                               title='Bootstrap',
                               message=content,
                               data=f_data)
    else:
        return abort(404)




@app.route(f"/サイトポリシー")
def site_policy():
    return render_template("index.html",
                           title="サイトポリシー",
                           message="サイトポリシー",
                           data=f_data)


@app.route(f"/プライバシーポリシー")
def privacy_policy():
    return render_template("index.html",
                           title="プライバシーポリシー",
                           message="プライバシ",
                           data=f_data)


@app.route(f"/サイトマップ")
def site_map():
    return render_template("index.html",
                           title="サイトマップ",
                           message="サイトマップ",
                           data=f_data)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5222, threaded=True)  # Webアプリケーションの起動
