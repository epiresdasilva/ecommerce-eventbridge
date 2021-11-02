import json
import boto3


client = boto3.client('events')


def main(event, context):
    print("Despacho Incluir Pendencia: ", str(event["detail"]))

    event_response = client.put_events(
        Entries=[
            {
                'Source': 'DespachoIncluido',
                'DetailType': 'Despacho Incluido',
                'Detail': str(event["body"]),
                'EventBusName': 'ecommerce-event-bridge-bus'
            },
        ]
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(event_response)
    }

    return response
