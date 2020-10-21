# project/api/crud.py


from project import db
from project.api.models import Subscriber

'''get subscriber by id from db'''
def get_subscriber_by_id(subscriber_id):
    return Subscriber.query.filter_by(id=subscriber_id).first()

'''get subscriber by email from db'''
def get_subscriber_by_email(email):
    return Subscriber.query.filter_by(email=email).first()

'''add subscriber to db'''
def add_subscriber(name, email):
    subscriber = Subscriber(name=name, email=email)
    db.session.add(subscriber)
    db.session.commit()
    return subscriber

'''delete subscriber from db'''
def delete_subscriber(subscriber):
    db.session.delete(subscriber)
    db.session.commit()
    return subscriber
