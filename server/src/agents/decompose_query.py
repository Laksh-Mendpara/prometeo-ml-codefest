from composio_openai import ComposioToolSet, App
from openai import OpenAI
from config import (
    QUERY_DECOMPOSITION_SYSTEM_MESSAGE,
    QUERY_DECOMPOSITION_USER_PROMPT,
)
from typing import List
import os
from loguru import logger
from dotenv import load_dotenv
load_dotenv()

def decompose_query_into_subqueries(query: str, available_apps: List[str]) -> List[str]:
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    composio_toolset = ComposioToolSet()

    tools = composio_toolset.get_tools(apps=available_apps)

    user_message = QUERY_DECOMPOSITION_USER_PROMPT.format(
        user_query=query
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        tools=tools,
        messages=[
            {"role": "system", "content": QUERY_DECOMPOSITION_SYSTEM_MESSAGE},
            {"role": "user", "content": user_message},
        ],
    ).choices[0].message.content
    response = response.split("[")[1]
    response = response.split("]")[0]
    logger.debug(f"Response from decomposition client: {response}")

    # Parse and return the decomposed sub-queries as a list
    import json
    sub_queries = json.loads("[" + response + "]")  # Assuming JSON array is returned
    logger.debug(f"Decomposed sub-queries: {sub_queries}")
    logger.debug(f"response type: {type(sub_queries)}")
    return sub_queries


if __name__ == "__main__":
    query = "Star the repo composio on GitHub and mail the contributors"
    from routeApps import route_apps
    available_apps = route_apps(query)
    result = decompose_query_into_subqueries(query, available_apps)
    logger.info(result)
