import json
import os
import datetime
import uuid
from http import HTTPStatus
from broker.redis_broker import RedisBroker
from adapters.cache_adapter import CacheAdapter
from resources.utils.position_utils import PostitionUtils
from constants import Constants


class LambdaExecution():

    def __init__(self, factory: CacheAdapter):
        self.factory = factory

    def execute_post(self, body, name):
        self.factory.set_data(name, body)

    def execute_get(self):
        response = {
            "isBase64Encoded": True,
            "statusCode": HTTPStatus.OK,
            "headers": {},
            "multiValueHeaders": {},
            "body": {}
        }
        
        kenoby = bool(self.factory.valid_key(Constants.kenoby['satellite_name']))
        skywalker = bool(self.factory.valid_key(Constants.skywalker['satellite_name']))
        sato = bool(self.factory.valid_key(Constants.sato['satellite_name']))

        if(kenoby is not True or skywalker is not True or sato is not True):

            response['statusCode'] = HTTPStatus.BAD_REQUEST
            response['body'] = "Missing some locations."
            return response
        
        kenoby = json.loads(
            self.factory.get_data(
                Constants.kenoby['satellite_name']))
        skywalker = json.loads(
            self.factory.get_data(
                Constants.skywalker['satellite_name']))
        sato = json.loads(
            self.factory.get_data(
                Constants.sato['satellite_name']))


        if (len(kenoby['message']) != len(skywalker['message'])
           or len(skywalker['message']) != len(sato['message'])):
            response['statusCode'] = HTTPStatus.BAD_REQUEST
            response['body'] = "Messages are not the same size."
            return response

        location = PostitionUtils().get_locations(
            kenoby['distance'],
            skywalker['distance'],
            sato['distance'],
        )

        response['body'] = {
            'location': {'x': location[0], 'y':location[1]},
            'message': PostitionUtils().get_message(kenoby['message'],
                                                    skywalker['message'],
                                                    sato['message'])
            }

        response['body'] = json.dumps(response['body'])

        return response


def lambda_handler(event, context):
    response = {
        "isBase64Encoded": True,
        "statusCode": HTTPStatus.OK,
        "headers": {},
        "multiValueHeaders": {},
        "body": {}
    }

    url = os.environ.get('cache_url')
    redis = RedisBroker(url)
    lambda_exec = LambdaExecution(redis)
    
    try:
        if(event['httpMethod'] == "POST"):
            lambda_exec.execute_post(str(event['body']),
                                     event['pathParameters']['satellite_name'])
            response['body'] = "Saved position."
            return response
        else:
            return lambda_exec.execute_get()
    except Exception as ex:
        response = {
            "statusCode": HTTPStatus.INTERNAL_SERVER_ERROR,
            "body": "Error has occurred: {}.".format(str(ex))
        }
        return response
