#import boto3
from decimal import Decimal
import os


def lambda_handler(event,context):
    #table.put_item(Item=event) #for posting
    item = 0
    
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(os.environ["TABLE_NAME"])
        
        
        table.update_item(Key={'id': '1'},
            UpdateExpression='SET hcount = hcount + :val1',
            ExpressionAttributeValues={
                ':val1': Decimal(1)
            },
            ReturnValues="UPDATED_NEW"
        )
        
        response = table.get_item(Key={'id': '1'})
        item = response['Item']['hcount']
    except Exception as e: print(e)
    
    
    return {
        "isBase64Encoded": "false",
        "statusCode": 200,
        "headers": { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Credentials" : "true" },
        "body": item
        }
