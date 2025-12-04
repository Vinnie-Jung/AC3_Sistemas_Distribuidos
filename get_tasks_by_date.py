import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    date = event["pathParameters"]["date"]

    response = table.query(
        IndexName="date-index",
        KeyConditionExpression=Key("date").eq(date)
    )

    items = response.get("Items", [])

    return {
        "statusCode": 200,
        "body": json.dumps(items)
    }
