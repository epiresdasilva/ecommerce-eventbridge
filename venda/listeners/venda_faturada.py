def main(event, context):
    print("Venda Faturada: ", str(event))

    return {
        "message": "Venda Faturada",
        "event": event
    }
