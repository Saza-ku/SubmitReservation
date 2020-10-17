from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'#←ここ？
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.String(10), primary_key=True, nullable=False)
    password = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, id, password):
        self.id = id
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username