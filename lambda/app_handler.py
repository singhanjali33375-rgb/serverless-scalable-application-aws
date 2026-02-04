import json
from db_utils import save_data

def lambda_handler(event, context):
    body = event.get("body", {})
    result = save_data(body)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Request processed successfully",
            "data": result
        })
    }
