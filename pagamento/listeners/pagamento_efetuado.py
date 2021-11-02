def main(event, context):
    print("Pagamento Efetuado: ", str(event))

    return {
        "message": "Pagamento Efetuado",
        "event": event
    }
