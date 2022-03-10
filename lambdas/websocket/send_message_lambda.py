import boto3

client = boto3.client('apigatewaymanagementapi',
                      endpoint_url='https://2n27czi3oa.execute-api.us-east-1.amazonaws.com/dev/@connections')


def send_message():
    response = client.post_to_connection(
        Data='some data',
        ConnectionId='Ox69Gei9IAMCFqQ='
    )
    print(response)


send_message()
