import logging
import requests
import random
import azure.functions as func
from azure.cosmos import exceptions, CosmosClient, PartitionKey


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    """
    endpoint = "endpoint"
    key = 'primary_key'
    
    #<create cosmos client>
    client = CosmosClient(endpoint, key)
    #</create_cosmos_clients>
    database_name = 'usernames'
    database = client.create_database_if_not_exists(id=database)
    container_name = 'UsernamesContainer'
    container = database.create_container_if_not_exists(
        id=container_name
        partition_key=PartitionKey(path="/username")
        offer_throughput=400
    )
    """

    logging.info('Python HTTP trigger function processed a request.')

    numbers = requests.get("published_link_to_server2")
    letters = requests.get("published_link_to_server3")


    combined = numbers.text + letters.text
    loggin.info(numbers.text)
    logging.info(letters.text)

    """
    items_to_add ={
            "id": str(random.randint(0,100)),
            "username": combined
        }
    container.create_item(body=item_to_add)
    """
    
    return func.HttpResponse(
             combined,
             status_code=200
        )
