def main(event, context):
    print("Venda Incluida: ", str(event))

    return {
        "message": "Venda Incluida",
        "event": event
    }
