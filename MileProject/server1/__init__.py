import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    numbers = requests.get("")
    letters = requests.get("")

    username = str(numbers.text) + letters.text

    if username:
        return func.HttpResponse(f"Username: {username}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully.",
             status_code=200
        )
