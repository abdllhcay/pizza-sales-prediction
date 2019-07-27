from api import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    started = db.Column(db.String)
    finished = db.Column(db.String)
    status = db.Column(db.String)
    step = db.Column(db.Integer)
    file_path = db.Column(db.String)
    result = db.Column(db.String)

    @property
    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "started": self.started,
            "finished": self.finished,
            "status": self.status,
            "step": self.step,
            "file_path": self.file_path,
            "result": self.result
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True,)
    password = db.Column(db.String)

    @property
    def serialize(self):
        return{
            "id": self.id,
            "username": self.username,
            "password": self.password
        }