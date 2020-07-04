import boto3
import json

#print('Loading function')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
        
     return {"code":200,
           "message":"return, at lamdba handler fired"
    }


