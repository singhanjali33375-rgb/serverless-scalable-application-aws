import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("ServerlessAppTable")

def save_data(data):
    table.put_item(Item=data)
    return data
