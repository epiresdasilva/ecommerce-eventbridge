def main(event, context):
    print("Pedido Incluido: ", str(event))

    return {
        "message": "Pedido Incluido",
        "event": event
    }
