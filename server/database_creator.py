from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin

engine = create_engine('sqlite:///pizza-sales-prediction.db', echo=True)
Base = declarative_base()

class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    started = Column(String)
    finished = Column(String)
    status = Column(String)
    step = Column(Integer)
    file_path = Column(String)
    result = Column(String)

    def __init__(self, name, started, finished, status, step, file_path, result):
        self.name = name
        self.started = started
        self.finished = finished
        self.status = status
        self.step = step
        self.file_path = file_path
        self.result = result

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True,)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

Base.metadata.create_all(engine)