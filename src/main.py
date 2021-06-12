import json


def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps("resume-api lambda function is working")
    }
