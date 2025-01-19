from routeApps import route_apps
from query_type import is_multihop_query
from simple_query import process_simple_query
from multihop_query import process_mulit_hop_query
from typing_extensions import List
from loguru import logger
from dotenv import load_dotenv
load_dotenv()

def process_query(query: str, context: str="")-> str:
    available_apps = route_apps(query)
    logger.info(f"available_apps: {available_apps}")
    query_type = is_multihop_query(query, available_apps)
    logger.info(f"query_type: {query_type}")
    if query_type == 0:
        result = process_simple_query(query, available_apps, context)
    else:
        result = process_mulit_hop_query(query, available_apps, context)
    logger.info(result)
    return result

if __name__ == "__main__":
    task = str(input("Enter your Task: "))
    result = process_query(task)
