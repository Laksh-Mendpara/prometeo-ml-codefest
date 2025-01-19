from composio import ComposioToolSet, App
from openai import OpenAI
from config import (
    ROUTE_SYSTEM_MESSAGE,
    ROUTE_USER_PROMPT
)
from typing_extensions import List, Dict
from loguru import logger
import os
from dotenv import load_dotenv
load_dotenv()

def route_apps(query: str) -> List:    

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    toolset = ComposioToolSet(api_key=os.getenv("COMPOSIO_API_KEY"))

    apps = toolset.get_apps()
    apps = [app.name for app in apps]
    apps = ", ".join(apps)
    logger.debug(f"Available apps: {apps}")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": ROUTE_SYSTEM_MESSAGE},
            {
                "role": "user", 
                "content": ROUTE_USER_PROMPT.format(user_query=query, available_apps=apps)
            },
        ]
    ).choices[0].message.content.upper()

    logger.debug(f"Response of route App client: {response}")
    app_names = response.split(", ")
    apps = [getattr(App, app_name) for app_name in app_names if hasattr(App, app_name)]
    logger.debug(f"Apps: {apps}")
    return apps


if __name__ == "__main__":
    query = "Star the repo composiohq/composio on GitHub and create a mail"
    result = route_apps(query)
    logger.info(result)
