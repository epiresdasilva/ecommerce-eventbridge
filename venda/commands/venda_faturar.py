import json
import boto3
import json


client = boto3.client('events')


def main(event, context):
    print("Venda Faturar: ", str(event["detail"]))

    event_response = client.put_events(
        Entries=[
            {
                'Source': 'Faturado',
                'DetailType': 'Faturado',
                'Detail': json.dumps(event["detail"]),
                'EventBusName': 'ecommerce-event-bridge-bus'
            },
        ]
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(event_response)
    }

    return response
