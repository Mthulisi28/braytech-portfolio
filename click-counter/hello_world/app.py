import json, os, boto3
dynamodb = boto3.resource('dynamodb')
table   = dynamodb.Table(os.environ['COUNTER_TABLE'])

def post_click(event, context):
    resp = table.update_item(
        Key={'id': 'counter'},
        UpdateExpression='ADD clicks :inc',
        ExpressionAttributeValues={':inc': 1},
        ReturnValues='UPDATED_NEW'
    )
    total = resp['Attributes']['clicks']
    return {'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'clicks': int(total)})}

def get_clicks(event, context):
    resp = table.get_item(Key={'id': 'counter'})
    total = resp.get('Item', {}).get('clicks', 0)
    return {'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'clicks': int(total)})}
