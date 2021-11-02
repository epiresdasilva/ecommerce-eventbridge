def main(event, context):
    print("Venda Despachada: ", str(event))

    return {
        "message": "Venda Despachada",
        "event": event
    }
