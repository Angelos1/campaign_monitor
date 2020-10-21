# project/api/models.py


from sqlalchemy.sql import func

from project import db


class Subscriber(db.Model):

    __tablename__ = "subscribers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email
