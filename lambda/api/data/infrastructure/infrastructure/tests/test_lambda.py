from lambda.app_handler import lambda_handler

def test_lambda_handler():
    event = {"body": {"userId": "101"}}
    response = lambda_handler(event, None)
    assert response["statusCode"] == 200
