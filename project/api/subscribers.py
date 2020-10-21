# project/api/subscribers.py
import os

from flask import Blueprint, request
from flask_restx import Api, Resource, fields
from project.api.crud import (
    get_subscriber_by_id,
    get_subscriber_by_email,
    add_subscriber,
    delete_subscriber,
)
from project.api.campaignmonitor import (
    get_campaign_list_by_id,
    add_subscriber_to_email_list,
    remove_subscriber_from_email_list,

)

subscribers_blueprint = Blueprint("subscribers", __name__)
api = Api(subscribers_blueprint)

subscriber = api.model(
    "Subscriber",
    {
        "id": fields.Integer(readOnly=True),
        "name": fields.String(required=True),
        "email": fields.String(required=True),
        "created_date": fields.DateTime,
    },
)


class CampaignList(Resource):
    @api.marshal_with(subscriber, as_list=True)
    def get(self, campaign_id):
        return get_campaign_list_by_id(campaign_id)



class Subscribers(Resource):
    @api.marshal_with(subscriber) # serializing subscriber to json
    def get(self, subscriber_id):
        subscriber = get_subscriber_by_id(subscriber_id)
        if not subscriber:
            api.abort(404, f"User {subscriber_id} does not exist")
        return subscriber, 200

    def post(self,list_id):
        post_data = request.get_json()
        email = post_data.get("EmailAddress")
        name = post_data.get("Name")
        response_object = {}
        subscriber = get_subscriber_by_email(email)
        if subscriber:
            response_object["message"] = "Sorry. That email already exists."
            return response_object, 400
        response = add_subscriber_to_email_list(name, email, list_id) #calling campaign monitor api
        if (response.status_code == 201):   #if created
            add_subscriber(name, email) # only if subscriber is added in campaign monitor will be added in our db
            return response.json()
        else:
            return response.status_code

    # def post(self, list_id):
    #
    #     return {"x": os.environ.get("API_KEY")}, 201
    #
    #     post_data = request.get_json()
    #     email = post_data.get("EmailAddress")
    #     name = post_data.get("Name")
    #     response = add_subscriber_to_email_list(name, email, list_id)  # calling campaign monitor api
    #     return response.json()

    def delete(self, list_id):
        response_object = {}
        email= ' '   # , subscriber_email get from query param
        subscriber = get_subscriber_by_email(email)  # updated
        if not subscriber:
            api.abort(404, f"User {email} does not exist")
        delete_subscriber(subscriber)
        remove_subscriber_from_email_list(email,list_id)
        response_object["message"] = f"{subscriber.email} was removed!"
        return response_object, 200



api.add_resource(CampaignList, "/campaign/<string:campaign_id>")
api.add_resource(Subscribers, "/subscribers/<string:list_id>")