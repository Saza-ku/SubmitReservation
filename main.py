from flask import *  # 必要なライブラリのインポート

app = Flask(__name__)  # アプリの設定

# @app.route("/")  # どのページで実行する関数か設定
# def main():
#     return "Hello, World!"  # Hello, World! を出力

#views
@app.route('/')
def view_home():
  return render_template(
    'index.html'
  )

@app.route('/signup')
def view_signup():
  return render_template(
    'signup.html'
  )

#auth
@app.route('/signup')
def signup():
    username = request.form('username')

@app.route('/login')
def login():
    pass

if __name__ == "__main__":  # 実行されたら
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)  # デバッグモード、localhost:8888 で スレッドオンで実行