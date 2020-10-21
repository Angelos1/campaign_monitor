# project/api/crud.py

import requests
import os
from requests.auth import HTTPBasicAuth

apikey = os.environ.get("API_KEY") # API key for campaign monitor

# def get_email_list_details_by_id(list_id):
#     url = f"https://api.createsend.com/api/v3.2/lists/{list_id}.json"
#     response = requests.request("GET", url, auth=HTTPBasicAuth(apikey, ''))
#     return response

'''Calls the campaignmonitor API that brings the lists for a campaign'''
def get_campaign_list_by_id(campaign_id):
    url = f"https://api.createsend.com/api/v3.2/campaigns/{campaign_id}/listsandsegments.json"
    response = requests.request("GET", url, auth=HTTPBasicAuth(apikey, ''))
    return response

'''Calls the campaignmonitor API that adds a subscriber in a list'''
def add_subscriber_to_email_list(name, email, list_id):
    url = f"https://api.createsend.com/api/v3.2/subscribers/{list_id}.json"

    payload = {"EmailAddress": email, "Name": name, "CustomFields": [], "Resubscribe": True,
               "RestartSubscriptionBasedAutoresponders": True, "ConsentToTrack": 'Yes'}

    response = requests.request("POST", url, auth=HTTPBasicAuth(apikey, ''), data=payload)
    return response

# def add_subscriber_to_email_list(name, email, list_id):
#     url = f"http://localhost:5001/subscribers/88751fe090ae4a35bd4b938f0d237588"
#     payload = {"EmailAddress": email, "Name": name, "CustomFields": [], "Resubscribe": True,
#                "RestartSubscriptionBasedAutoresponders": True, "ConsentToTrack": 'Yes'}
#     response = requests.request("PUT", url, auth=HTTPBasicAuth(apikey, ''), data=payload)
#     return response


'''Calls the campaignmonitor API that deletes a subscriber from a list'''
def remove_subscriber_from_email_list( email,list_id):
    url = f"https://api.createsend.com/api/v3.2/subscribers/{list_id}.json?email={email}"
    response = requests.request("DELETE", url, auth=HTTPBasicAuth(apikey, ''))
    return response



# def update_user(user, username, email):
#     user.username = username
#     user.email = email
#     db.session.commit()
#     return user


