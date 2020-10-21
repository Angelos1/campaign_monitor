# project/api/crud.py

import requests
import os
from project.api.models import Subscriber
from requests.auth import HTTPBasicAuth

apikey = os.environ.get("API_KEY")

def get_email_list_details_by_id(list_id):
    url = f"https://api.createsend.com/api/v3.2/lists/{list_id}.json"
    response = requests.request("GET", url, auth=HTTPBasicAuth(apikey, ''))
    return response

def get_campaign_list_by_id(campaign_id):
    url = f"https://api.createsend.com/api/v3.2/campaigns/{campaignid}/listsandsegments.json"
    response = requests.request("GET", url, auth=HTTPBasicAuth(apikey, ''))
    return response


def add_subscriber_to_email_list(name, email, list_id):
    url = f"https://api.createsend.com/api/v3.2/subscribers/{list_id}.json"
    response = requests.request("POST", url, auth=HTTPBasicAuth(apikey, ''))
    return response

def remove_subscriber_from_email_list( email,list_id):
    url = f"https://api.createsend.com/api/v3.2/subscribers/{list_id}.json?email={email}"
    response = requests.request("DELETE", url, auth=HTTPBasicAuth(apikey, ''))
    return response



# def update_user(user, username, email):
#     user.username = username
#     user.email = email
#     db.session.commit()
#     return user


