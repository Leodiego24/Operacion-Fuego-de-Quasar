import json
import unittest
from http import HTTPStatus
from lambda_function import LambdaExecution
from adapters.cache_adapter import CacheAdapter
from broker.redis_broker import RedisBroker


class TestLambdaFunctionSplit(unittest.TestCase):
    """Class with unit test"""
    kenoby = {
            "name": "kenoby",
            "distance": 100,
            "message": [
                "este",
                "",
                "",
                "mensaje",
                ""
            ]
        }

    skywalker = {
            "name": "skywalker",
            "distance": 115.5,
            "message": [
                "",
                "es",
                "",
                "",
                "secreto"
            ]
        }

    sato = {
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

    def __init__(self, methodName='runTest', param=None) -> None:
        """Contructor of test case"""
        super().__init__(methodName=methodName)
        redis_url = "ec2-34-228-141-225.compute-1.amazonaws.com"
        redis = RedisBroker(redis_url)
        self.lambda_exec = LambdaExecution(redis)

    def test_post_kenoby(self):
        """Test case save kenoby"""
        response = self.lambda_exec.execute_post(json.dumps(self.kenoby), "kenoby")
        self.assertEqual(response['statusCode'], HTTPStatus.OK)

    def test_post_skywalker(self):
        """Test case save skywalker"""
        response = self.lambda_exec.execute_post(json.dumps(self.skywalker), "skywalker")
        self.assertEqual(response['statusCode'], HTTPStatus.OK)

    def test_post_sato(self):
        """Test case save sato"""
        response = self.lambda_exec.execute_post(json.dumps(self.sato), "sato")
        self.assertEqual(response['statusCode'], HTTPStatus.OK)

    def test_correct(self):
        """Test case validation correct"""
        self.lambda_exec.execute_post(json.dumps(self.kenoby), "kenoby")
        self.lambda_exec.execute_post(json.dumps(self.skywalker), "skywalker")
        self.lambda_exec.execute_post(json.dumps(self.sato), "sato")
        response = self.lambda_exec.execute_get()
        self.assertEqual(response['statusCode'], HTTPStatus.OK)


if __name__ == "__main__":
    unittest.main()