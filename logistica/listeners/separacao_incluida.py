def main(event, context):
    print("Separacao Incluida: ", str(event))

    return {
        "message": "Separacao Incluida",
        "event": event
    }
