def main(event, context):
    print("Pedido Expirado: ", str(event))

    return {
        "message": "Pedido Expirado",
        "event": event
    }
