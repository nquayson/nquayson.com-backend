import boto3
from decimal import Decimal


def lambda_handler(event,context):
    #table.put_item(Item=event) #for posting
    item = 0
    
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('data1')
        
        
        table.update_item(Key={'id': '1'},
            UpdateExpression='SET ip = ip + :val1',
            ExpressionAttributeValues={
                ':val1': Decimal(1)
            },
            ReturnValues="UPDATED_NEW"
        )
        
        response = table.get_item(Key={'id': '1'})
        item = response['Item']['ip']
    except Exception as e: print(e)
    
    return {"code":200, 
            "count":item,
           "message":"Add success"
    }

##
#result = {'code': 200, 'message': 'return, at lamdba handler fired'}
#result = {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
#result = lambda_handler("hi", "hi")
#print (result['child1']['year'])
