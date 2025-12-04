import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    task_id = event["pathParameters"]["task_id"]
    
    response = table.get_item(Key={"task_id": task_id})
    item = response.get("Item")

    if not item:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "Task not found"})
        }

    return {
        "statusCode": 200,
        "body": json.dumps(item)
    }
