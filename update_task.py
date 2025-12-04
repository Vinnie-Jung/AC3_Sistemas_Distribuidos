import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    task_id = event["pathParameters"]["task_id"]
    body = json.loads(event["body"])

    table.update_item(
        Key={"task_id": task_id},
        UpdateExpression="SET title = :t, description = :d, #dt = :date",
        ExpressionAttributeNames={ "#dt": "date" },
        ExpressionAttributeValues={
            ":t": body["title"],
            ":d": body["description"],
            ":date": body["date"]
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Task updated"})
    }
