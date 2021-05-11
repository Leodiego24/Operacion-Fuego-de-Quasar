import json
import unittest
from http import HTTPStatus
from lambda_function import LambdaExecution


class TestLambdaFunction(unittest.TestCase):
    """Class with unit test"""
    body = {
            "satellites": [
                {
                    "name": "kenoby",
                    "distance": 100,
                    "message": [
                        "este",
                        "",
                        "",
                        "mensaje",
                        ""
                    ]
                },
                {
                    "name": "skywalker",
                    "distance": 115.5,
                    "message": [
                        "",
                        "es",
                        "",
                        "",
                        "secreto"
                    ]
                },
                {
                    "name": "sato",
                    "distance": 142.7,
                    "message": [
                        "este",
                        "",
                        "un",
                        "",
                        ""
                    ]
                }
            ]
        }

    def test_correct(self):
        """Test case validation correct"""
        response = LambdaExecution().execute_lambda(json.dumps(self.body))
        self.assertEqual(response['statusCode'], HTTPStatus.OK)
    
    def test_two_elements(self):
        """Test case validation two elements"""
        two_elements = self.body
        del two_elements['satellites'][-1]
        response = LambdaExecution().execute_lambda(json.dumps(two_elements))
        self.assertEqual(response['statusCode'], HTTPStatus.BAD_REQUEST)

    def test_message_incomplete(self):
        """Test case validation incomplete"""
        elements = self.body
        elements['satellites'][0]['message'] = ""
        response = LambdaExecution().execute_lambda(json.dumps(elements))
        self.assertEqual(response['statusCode'], HTTPStatus.BAD_REQUEST)

    def test_exception(self):
        """Test case validation exeption"""
        elements = {"body": "exception"}
        response = LambdaExecution().execute_lambda(json.dumps(elements))
        self.assertEqual(response['statusCode'], HTTPStatus.INTERNAL_SERVER_ERROR)

if __name__ == "__main__":
    unittest.main()