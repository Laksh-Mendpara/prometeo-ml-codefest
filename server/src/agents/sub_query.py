from composio_openai import ComposioToolSet
from openai import OpenAI
from typing_extensions import List, Dict
from config import QUERY_PROCESS_LLM_SYS_PROMPT
from loguru import logger
import os
from dotenv import load_dotenv
load_dotenv()

def get_subquery_tool(sub_query: str, available_apps: List, context: str = "") -> str:    

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    composio_toolset = ComposioToolSet()

    tools = composio_toolset.get_tools(
        apps = available_apps
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        tools=tools,
        messages=[
            {"role": "system", "content": QUERY_PROCESS_LLM_SYS_PROMPT.format(context=context)},
            {"role": "user", "content": sub_query},
        ],
    ).choices[0].message.tool_calls
    tool_call = [res.function for res in response]
    return str(tool_call)


if __name__ == "__main__":
    query = "Star the repo composio on GitHub"
    from routeApps import route_apps
    available_apps = route_apps(query)
    result = get_subquery_tool(query, available_apps)
    logger.info(result)
