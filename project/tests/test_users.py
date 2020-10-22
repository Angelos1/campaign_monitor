import json
from project.api.models import Subscriber
import project.api.subscribers
from requests.models import Response

'''Testing the call of /subscribers/88751fe090ae4a35bd4b938f0d237588 endpoint,
for adding a subscriber in a list. This is the case where the subscriber does
not already exists and he is actually added to the list
'''
def test_add_subscriber(test_app, test_database, monkeypatch):

    # constructing a mock response for campaignmonitor api (add subscriber to list api)
    the_response = Response()
    the_response.status_code = 201
    the_response._content = b'"subscriber@example.com"'

    # mocking the campaign monitor "add subscriber to list api" api for response because I cannot call it
    def mock_add_subscriber_to_email_list(name, email, list_id):
        return the_response

    # Replace add_subscriber_to_email_list with mock_add_subscriber_to_email_list
    monkeypatch.setattr(project.api.subscribers, "add_subscriber_to_email_list", mock_add_subscriber_to_email_list)

    client = test_app.test_client() # Flask client

    resp = client.post(
        "/subscribers/88751fe090ae4a35bd4b938f0d237588",
        data=json.dumps({"name": "michael", "email": "subscriber@example.com"}),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert "subscriber@example.com" in data["message"]
    assert resp.status_code == 201
