import json
import pytest
from project.api.models import Subscriber
import project.api.subscribers
from requests.models import Response

def test_add_subscriber(test_app, test_database, monkeypatch):

    the_response = Response()
    the_response.status_code = 201
    the_response._content = "subscriber@example.com"

    def mock_add_subscriber_to_email_list(name, email, list_id):
        return the_response

    monkeypatch.setattr(project.api.subscribers, "add_subscriber_to_email_list", mock_add_subscriber_to_email_list)
    # monkeypatch.setattr(project.api.subscribers, "add_user", mock_add_user)

    client = test_app.test_client()
    resp = client.post(
        "/subscribers/88751fe090ae4a35bd4b938f0d237588",
        data=json.dumps({"name": "michael", "email": "subscriber@example.com"}),

    )

    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert "subscriber@example.com" in data["message"]

#
# def test_single_subscriber(test_app, test_database, add_subscriber):
#     subscriber = add_subscriber("jeffrey", "jeffrey@testdriven.io")
#     client = test_app.test_client()
#     resp = client.get(f"/subscribers/{subscriber.id}")
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 200
#     assert "jeffrey" in data["name"]
#     assert "jeffrey@testdriven.io" in data["email"]
#
#
# def test_single_subscriber_incorrect_id(test_app, test_database):
#     client = test_app.test_client()
#     resp = client.get("/subscribers/999")
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 404
#     assert "subscriber 999 does not exist" in data["message"]
#
#
# def test_all_subscribers(test_app, test_database, add_subscriber):
#     test_database.session.query(Subscriber).delete()
#     add_subscriber("michael", "michael@mherman.org")
#     add_subscriber("fletcher", "fletcher@notreal.com")
#     client = test_app.test_client()
#     resp = client.get("/subscribers")
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 200
#     assert len(data) == 2
#     assert "michael" in data[0]["name"]
#     assert "michael@mherman.org" in data[0]["email"]
#     assert "fletcher" in data[1]["name"]
#     assert "fletcher@notreal.com" in data[1]["email"]
#
#
# def test_add_subscriber(test_app, test_database):
#     client = test_app.test_client()
#     resp = client.post(
#         "/subscribers",
#         data=json.dumps({"name": "michael", "email": "michael@testdriven.io"}),
#         content_type="application/json",
#     )
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 201
#     assert "michael@testdriven.io was added!" in data["message"]
#
#
# def test_add_subscriber_invalid_json(test_app, test_database):
#     client = test_app.test_client()
#     resp = client.post("/subscribers", data=json.dumps({}), content_type="application/json",)
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 400
#     assert "Input payload validation failed" in data["message"]
#
#
# def test_add_subscriber_invalid_json_keys(test_app, test_database):
#     client = test_app.test_client()
#     resp = client.post(
#         "/subscribers",
#         data=json.dumps({"email": "john@testdriven.io"}),
#         content_type="application/json",
#     )
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 400
#     assert "Input payload validation failed" in data["message"]
#
#
# def test_add_subscriber_duplicate_email(test_app, test_database):
#     client = test_app.test_client()
#     client.post(
#         "/subscribers",
#         data=json.dumps({"name": "michael", "email": "michael@testdriven.io"}),
#         content_type="application/json",
#     )
#     resp = client.post(
#         "/subscribers",
#         data=json.dumps({"name": "michael", "email": "michael@testdriven.io"}),
#         content_type="application/json",
#     )
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 400
#     assert "Sorry. That email already exists." in data["message"]
#
#
# def test_remove_subscriber(test_app, test_database, add_subscriber):
#     test_database.session.query(Subscriber).delete()
#     subscriber = add_subscriber("subscriber-to-be-removed", "remove-me@testdriven.io")
#     client = test_app.test_client()
#     resp_one = client.get("/subscribers")
#     data = json.loads(resp_one.data.decode())
#     assert resp_one.status_code == 200
#     assert len(data) == 1
#     resp_two = client.delete(f"/subscribers/{subscriber.id}")
#     data = json.loads(resp_two.data.decode())
#     assert resp_two.status_code == 200
#     assert "remove-me@testdriven.io was removed!" in data["message"]
#     resp_three = client.get("/subscribers")
#     data = json.loads(resp_three.data.decode())
#     assert resp_three.status_code == 200
#     assert len(data) == 0
#
#
# def test_remove_subscriber_incorrect_id(test_app, test_database):
#     client = test_app.test_client()
#     resp = client.delete("/subscribers/999")
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 404
#     assert "subscriber 999 does not exist" in data["message"]
#
#
# def test_update_subscriber(test_app, test_database, add_subscriber):
#     subscriber = add_subscriber("subscriber-to-be-updated", "update-me@testdriven.io")
#     client = test_app.test_client()
#     resp_one = client.put(
#         f"/subscribers/{subscriber.id}",
#         data=json.dumps({"name": "me", "email": "me@testdriven.io"}),
#         content_type="application/json",
#     )
#     data = json.loads(resp_one.data.decode())
#     assert resp_one.status_code == 200
#     assert f"{subscriber.id} was updated!" in data["message"]
#     resp_two = client.get(f"/subscribers/{subscriber.id}")
#     data = json.loads(resp_two.data.decode())
#     assert resp_two.status_code == 200
#     assert "me" in data["name"]
#     assert "me@testdriven.io" in data["email"]
#
#
# def test_update_subscriber_invalid_json(test_app, test_database):
#     client = test_app.test_client()
#     resp = client.put("/subscribers/1", data=json.dumps({}), content_type="application/json",)
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 400
#     assert "Input payload validation failed" in data["message"]
#
#
# def test_update_subscriber_invalid_json_keys(test_app, test_database):
#     client = test_app.test_client()
#     resp = client.put(
#         "/subscribers/1",
#         data=json.dumps({"email": "me@testdriven.io"}),
#         content_type="application/json",
#     )
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 400
#     assert "Input payload validation failed" in data["message"]
#
#
# def test_update_subscriber_does_not_exist(test_app, test_database):
#     client = test_app.test_client()
#     resp = client.put(
#         "/subscribers/999",
#         data=json.dumps({"name": "me", "email": "me@testdriven.io"}),
#         content_type="application/json",
#     )
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == 404
#     assert "subscriber 999 does not exist" in data["message"]
#
#     # This replaces the above 3 tests
#
#
# @pytest.mark.parametrize(
#     "subscriber_id, payload, status_code, message",
#     [
#         [1, {}, 400, "Input payload validation failed"],
#         [1, {"email": "me@testdriven.io"}, 400, "Input payload validation failed"],
#         [
#             999,
#             {"name": "me", "email": "me@testdriven.io"},
#             404,
#             "subscriber 999 does not exist",
#         ],
#     ],
# )
# def test_update_subscriber_invalid(
#     test_app, test_database, subscriber_id, payload, status_code, message
# ):
#     client = test_app.test_client()
#     resp = client.put(
#         f"/subscribers/{subscriber_id}", data=json.dumps(payload), content_type="application/json",
#     )
#     data = json.loads(resp.data.decode())
#     assert resp.status_code == status_code
#     assert message in data["message"]
