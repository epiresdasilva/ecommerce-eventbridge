import json
import boto3


client = boto3.client('events')


def main(event, context):
    print("Despacho Confirmar: ", event["body"])

    event_response = client.put_events(
        Entries=[
            {
                'Source': 'VendaDespachada',
                'DetailType': 'Venda Despachada',
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
