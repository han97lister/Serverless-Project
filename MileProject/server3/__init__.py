import logging
import random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    char = ""
    letters = "abcdefghijklmnopqrstuvwxyz"

    for i in range(4):
        char += letters[random.randint(0,25)]

    return func.HttpResponse(
            char,
            status_code=200
    )
