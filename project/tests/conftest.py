import pytest

from project import create_app, db
from project.api.models import Subscriber


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.config.from_object("project.config.TestingConfig")
    with app.app_context():
        yield app  # testing happens here


@pytest.fixture(scope="module")
def test_database():
    db.create_all()
    yield db  # testing happens here
    db.session.remove()
    db.drop_all()


@pytest.fixture(scope="function")
def add_subscriber():
    def _add_subscriber(name, email):
        subscriber = Subscriber(name=name, email=email)
        db.session.add(subscriber)
        db.session.commit()
        return subscriber

    return _add_subscriber
