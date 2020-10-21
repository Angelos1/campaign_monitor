# project/api/crud.py


from project import db
from project.api.models import Subscriber


# def get_all_users():
#     return Subscriber.query.all()
#
#

#
#
# def get_user_by_email(email):
#     return Subscriber.query.filter_by(email=email).first()

def get_subscriber_by_id(subscriber_id):
    return Subscriber.query.filter_by(id=subscriber_id).first()

def get_subscriber_by_email(email):
    return Subscriber.query.filter_by(email=email).first()

def add_subscriber(name, email):
    subscriber = Subscriber(name=name, email=email)
    db.session.add(subscriber)
    db.session.commit()
    return subscriber

def delete_subscriber(subscriber):
    db.session.delete(subscriber)
    db.session.commit()
    return subscriber

# def update_user(user, username, email):
#     user.username = username
#     user.email = email
#     db.session.commit()
#     return user


