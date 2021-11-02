import json
import boto3


client = boto3.client('events')


def main(event, context):
    print("Separacao Confirmar: ", event["body"])

    event_response = client.put_events(
        Entries=[
            {
                'Source': 'VendaSeparada',
                'DetailType': 'Venda Separada',
                'Detail': event["body"],
                'EventBusName': 'ecommerce-event-bridge-bus'
            },
        ]
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(event_response)
    }

    return response
