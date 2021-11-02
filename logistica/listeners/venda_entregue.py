def main(event, context):
    print("Venda Entregue: ", str(event))

    return {
        "message": "Venda Entregue",
        "event": event
    }
