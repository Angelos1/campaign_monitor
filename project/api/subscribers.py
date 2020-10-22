# project/api/subscribers.py


from flask import Blueprint, request
from flask_restx import Api, Resource, fields
from project.api.crud import (
    get_subscriber_by_id,
    get_subscriber_by_email,
    add_subscriber,
    delete_subscriber,
)
from project.api.campaign_monitor import (
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
    },
)

'''Http requests handling in the code below'''
class CampaignList(Resource):
    '''get all lists for a campaign'''
    def get(self, campaign_id):
        return get_campaign_list_by_id(campaign_id)

class Subscribers(Resource):
    '''add a subscriber'''
    def post(self,list_id):
        post_data = request.get_json()
        email = post_data.get("email")
        name = post_data.get("name")
        response_object = {}
        subscriber = get_subscriber_by_email(email)
        if subscriber:
            response_object["message"] = "Sorry. That email already exists."
            return response_object, 400
        campaign_response = add_subscriber_to_email_list(name, email, list_id)      #calling campaign monitor api
        response_object["message"] = campaign_response.json()
        if (campaign_response.status_code == 201):                       #if created # other validations should be added
            add_subscriber(name, email)       # only if subscriber is added in campaign monitor will be added in our db
            return response_object, 201
        else:
            return campaign_response

    # def put(self, list_id):
    #     post_data = request.get_json()
    #     return post_data
    #
    #     post_data = request.get_json()
    #     email = post_data.get("EmailAddress")
    #     name = post_data.get("Name")
    #     response = add_subscriber_to_email_list(name, email, list_id)  # calling campaign monitor api
    #     return response.json()

    # def delete(self, list_id):
    #     response_object = {}
    #     email = ' '   # , subscriber_email get from query param
    #     subscriber = get_subscriber_by_email(email)  #for quicker response we check in our db if subscriber not exists
    #     if not subscriber:
    #         api.abort(404, f"User {email} does not exist")
    #     delete_subscriber(subscriber) #remover subscriber from our db
    #     remove_subscriber_from_email_list(email, list_id) #remove subscriber from campaign monitor
    #     response_object["message"] = f"{subscriber.email} was removed!"
    #     return response_object, 200
    '''delete a subscriber'''
    def delete(self, list_id):
        email = request.args.get('email') #  get subscriber email from query param
        subscriber = get_subscriber_by_email(email)  # for quicker response we check in our db if subscriber not exists
        if not subscriber:
            api.abort(404, f"User {email} does not exist")
        response = remove_subscriber_from_email_list(email, list_id)  # remove subscriber from campaign monitor
        if (response.status_code == 200):
            delete_subscriber(subscriber)  # remover subscriber from our db
            return response.json()
        else:
            return response.json()

api.add_resource(CampaignList, "/campaign/<string:campaign_id>") #endpoint for Campaigns
api.add_resource(Subscribers, "/subscribers/<string:list_id>") #endpoint for subscribers