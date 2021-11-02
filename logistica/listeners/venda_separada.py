def main(event, context):
    print("Venda Separada: ", str(event))

    return {
        "message": "Venda Separada",
        "event": event
    }
