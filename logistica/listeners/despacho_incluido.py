def main(event, context):
    print("Despacho Incluido: ", str(event))

    return {
        "message": "Despacho Incluido",
        "event": event
    }
