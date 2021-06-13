import json
from src.resume_helper import get_resume


def lambda_handler(event, context):
    resume = get_resume()
    return {
        'statusCode': 200,
        'body': json.dumps(resume, default=lambda o: o.__dict__, sort_keys=False, indent=4)
    }
