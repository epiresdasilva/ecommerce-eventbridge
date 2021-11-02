import json
import boto3


client = boto3.client('events')


def main(event, context):
    print("Pagamento Incluir Pendente: ", str(event["detail"]))

    event_response = client.put_events(
        Entries=[
            {
                'Source': 'PagamentoIncluido',
                'DetailType': 'Pagamento Incluido',
                'Detail': str(event["detail"]),
                'EventBusName': 'ecommerce-event-bridge-bus'
            },
        ]
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(event_response)
    }

    return response
