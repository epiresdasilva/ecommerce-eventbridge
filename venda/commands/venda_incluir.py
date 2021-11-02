import json
import boto3


client = boto3.client('events')


def main(event, context):
    print("Venda Incluir: ", event["body"])

    event_response = client.put_events(
        Entries=[
            {
                'Source': 'VendaIncluida',
                'DetailType': 'Venda Incluida',
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
