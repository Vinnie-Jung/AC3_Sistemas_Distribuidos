import json
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    
    task_id = str(uuid.uuid4())
    
    item = {
        "task_id": task_id,
        "title": body["title"],
        "description": body["description"],
        "date": body["date"]
    }
    
    table.put_item(Item=item)
    
    return {
        "statusCode": 201,
        "body": json.dumps(item)
    }
