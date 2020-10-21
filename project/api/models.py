# project/api/models.py

import os
from flask_admin.contrib.sqla import ModelView
from project import db


class Subscriber(db.Model):

    __tablename__ = "subscribers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

'''enable admin interface if we are in development env'''
if os.getenv("FLASK_ENV") == "development":
    from project import admin
    admin.add_view(ModelView(Subscriber, db.session))