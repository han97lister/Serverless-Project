import logging
import random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    numbers = ""
    for i in range(4):
        numbers += str(random.randint(0,10))
    logging.info(numbers)

    return func.HttpResponse(
            numbers,
            status_code=200
    )
