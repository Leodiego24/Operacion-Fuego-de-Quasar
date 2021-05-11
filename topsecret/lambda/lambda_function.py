import json
import datetime
import uuid
from http import HTTPStatus
from resources.utils.position_utils import PostitionUtils
from constants import Constants


class LambdaExecution():
    """Class with all lambda execution"""

    def execute_lambda(self, params):
        """Method with lambda Execution"""
        response = {
            "isBase64Encoded": True,
            "statusCode": HTTPStatus.OK,
            "headers": {},
            "multiValueHeaders": {},
            "body": {}
        }
        
        try:
            params = json.loads(str(params))
            data =  params['satellites']
            
            if(len(data) != 3):
                response = {
                    "statusCode": HTTPStatus.BAD_REQUEST,
                    "body": "Missing some locations."
                    }
                return response
            
            locations = [item['distance'] for item in data]
            messages = [item['message'] for item in data]
        
            if (len(messages[0]) != len(messages[1]) or len(messages[1]) != len(messages[2])):
                response = {
                    "statusCode": HTTPStatus.BAD_REQUEST,
                    "body": "Messages are not the same size."
                    }
                return response

            location = PostitionUtils().get_locations(
                list(filter(lambda x: (x['name'] == Constants.kenoby['satellite_name']), data))[0]['distance'],
                list(filter(lambda x: (x['name'] == Constants.skywalker['satellite_name']), data))[0]['distance'],
                list(filter(lambda x: (x['name'] == Constants.sato['satellite_name']), data))[0]['distance']
            )

            response['body'] = {
                'location': {'x': location[0], 'y':location[1]},
                'message': PostitionUtils().get_message(messages[0], messages[1], messages[2])
                }
            response['body'] = json.dumps(response['body'])
            return response
        except Exception as ex:
            response = {
                "statusCode": HTTPStatus.INTERNAL_SERVER_ERROR,
                "body": "Error has occurred: {}.".format(str(ex))
            }
            return response    
    

def lambda_handler(event, context):
    """Lambda handler"""
    return LambdaExecution().execute_lambda(event['body'])
