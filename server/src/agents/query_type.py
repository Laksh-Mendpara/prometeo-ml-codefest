from composio_openai import ComposioToolSet
from openai import OpenAI
from config import (
    QUERY_TYPE_SYSTEM_MESSAGE,
    QUERY_TYPE_USER_PROMPT
)
from typing_extensions import List, Dict
from loguru import logger
import os
from dotenv import load_dotenv
load_dotenv()

def is_multihop_query(query: str, available_apps: List) -> List:    

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    composio_toolset = ComposioToolSet()

    tools = composio_toolset.get_tools(
        apps = available_apps
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        tools=tools,
        messages=[
            {"role": "system", "content": QUERY_TYPE_SYSTEM_MESSAGE},
            {
                "role": "user", 
                "content": QUERY_TYPE_USER_PROMPT.format(user_query=query)
            },
        ]
    ).choices[0].message.content

    logger.debug(f"Response of check-query-type client: {response}")

    return int(response)


if __name__ == "__main__":
    query = "Star the repo composio on GitHub"
    from routeApps import route_apps
    available_apps = route_apps(query)
    result = is_multihop_query(query, available_apps)
    logger.info(result)
