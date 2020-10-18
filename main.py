from flask import *  # 必要なライブラリのインポート
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from user import User, session

app = Flask(__name__)  # アプリの設定
app.secret_key = "b'Q\x08\xe1Nb\\\x9c\xc0\xa1\xdaABC\x94\xd5\x15\x13\xb3t\x1c\xcf\xba\x18\x05'"

# @app.route("/")  # どのページで実行する関数か設定
# def main():
#     return "Hello, World!"  # Hello, World! を出力

#views
@app.route('/', methods=['GET', 'POST'])
def login_access():
    if request.method == 'GET':
        return render_template(
            'index.html'
        )
    if request.method == 'POST':
        id = request.form['id']
        password = request.form['password']

        #エラーチェック
        error_message = None
        if not id:
            error_message = 'IDの入力は必須です'
        elif not password:
            error_message = 'パスワードの入力は必須です'

        user = session.querry(User).filter_by(name = 'id').first()

        #ユーザー名ミス
        if user.id is None:
            error_message = 'ユーザー名が正しくありません'
        #パスワードミス
        elif user.password != password:
            error_message = 'パスワードが正しくありません'

        #エラーを表示
        if error_message is not None:
            flash(error_message, category = 'alert alert-danger')
            return redirect(url_for('login_access'))

        #エラーがなければログイン完了
        session['user_id'] = user.id
        flash('{}さんとしてログインしました'.format(id), category = 'alert alert-info')
        #return redirect(url_for('view_home'))
        return render_template('login.html', id = user.id)


@app.route('/signup', methods=['GET', 'POST'])
def signup_access():
    if request.method == 'GET':
        return render_template(
            'signup.html'
        )
    if request.method == 'POST':
        id = request.form['id']
        password = request.form['password']

        #エラーチェック
        error_message = None
        if not id:
            error_message = 'IDの入力は必須です'
        elif not password:
            error_message = 'パスワードの入力は必須です'
        #重複をチェック
        existing_id = session.query(User).get(id)
        if existing_id:
            error_message = 'このIDはすでに登録されています'
        #ログインできるかチェック

        #エラーを表示
        if error_message is not None:
            flash(error_message, category = 'alert alert-danger')
            return redirect (url_for('signup_access'))

        #エラーがなければ登録
        user = User(id, password)
        session.add(user)
        session.commit()

        flash('登録が完了しました。ログインしてください。', category = 'alert alert-info')
        return redirect(url_for('login_access'))

@app.route('/logout')
def logout():
    """ログアウトする"""
    flash('ログアウトしました', category='alert alert-info')
    return redirect(url_for('login_access'))

@app.route('/home')
def view_home():
    pass

if __name__ == "__main__":  # 実行されたら
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)  # デバッグモード、localhost:8888 で スレッドオンで実行