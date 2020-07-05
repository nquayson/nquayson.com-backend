import boto3
import unittest
from lambda_function import lambda_handler


class TestLambda(unittest.TestCase):
    def test_lambda_handler(self):
        # Testing lambda function
        print ("Running unit test...")
        self.assertEqual(lambda_handler("status","test")["code"],200)
