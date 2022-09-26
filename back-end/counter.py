import boto3
import json

def get_count():
    db = boto3.resource("dynamodb")
    table = db.Table("macamresumecounter")

    response = table.get_item(
            Key={'Site': 0}
    )
    
    count = response["Item"]["Visits"]
    return(count)

def handler(event, context):
    db = boto3.resource("dynamodb")
    table = db.Table("macamresumecounter")

    # Increment value in table by 1
    response = table.update_item(
        Key = {"Site": 0},
        UpdateExpression = "ADD Visits :incr",
        ExpressionAttributeValues = {':incr': 1}
    )

    # Return HTTP request
    return {
        'statusCode': 200,
        'headers': { "Access-Control-Allow-Origin": "*" },
        'body': get_count()
    }