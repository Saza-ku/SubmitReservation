from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

engine = create_engine('sqlite:///database.db')  # database.db というデータベースを使うという宣言です
Base = declarative_base()  # データベースのテーブルの親です

class User(Base):  # PythonではUserというクラスのインスタンスとしてデータを扱います
    __tablename__ = 'users'  # テーブル名は users です
    id = Column(String(10), primary_key=True, nullable=False)
    password = Column(String(50), nullable=False)

    def __init__(self, id, password):
        self.id = id
        self.password = password

    def __repr__(self):
        return "User<{}, {}, {}>".format(self.id, self.password)

class Assignment(Base):
    __tablename__ = 'assignments'
    id = Column(String(40), primary_key=True, nullable=False)
    user_id = Column(String(10), nullable=False)
    name = Column(String(50), nullable=False)
    cource_name = name = Column(String(50), nullable=False)
    deadline = Column(DateTime, nullable=False)

    def __init__(self, user_id, name, cource_name, deadline):
        self.id = uuid.uuid4()
        self.user_id = user_id
        self.name = name
        self.cource_name = cource_name
        self.deadline = deadline

    def __repr__(self):
        return "Assignment<{}, {}, {}, {}, {}>".format(self.id, self.user_id, self.name, self.cource_name, self.deadline)

Base.metadata.create_all(engine)  # 実際にデータベースを構築します
SessionMaker = sessionmaker(bind=engine)  # Pythonとデータベースの経路です
session = SessionMaker()  # 経路を実際に作成しました