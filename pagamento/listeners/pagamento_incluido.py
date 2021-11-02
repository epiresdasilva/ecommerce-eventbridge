def main(event, context):
    print("Pagamento Incluido: ", str(event))

    return {
        "message": "Pagamento Incluido",
        "event": event
    }
