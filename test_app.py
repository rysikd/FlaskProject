from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import abort

app = Flask(__name__)    # Flaskインスタンス作成

f_data = ['サイトポリシー', 'プライバシーポリシー', 'サイトマップ']

@app.route('/', methods=['GET', 'POST'])
def login_page():
    global f_data

    if request.method == 'GET':
        return render_template('index.html', \
            title=__name__, \
            message='test作成hp', \
            data = f_data)

    elif request.method == 'POST':
        content = request.form.get('form')
        return render_template('index.html', \
            title = 'Bootstrap', \
            message=content, \
            data = f_data)
    else:
        return abort(404)

if __name__ == '__main__':
    app.run(debug=True, host = 'localhost', port=5222, threaded=True)    # Webアプリケーションの起動