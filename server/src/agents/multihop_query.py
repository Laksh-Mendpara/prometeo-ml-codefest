from composio_openai import ComposioToolSet, App
from openai import OpenAI
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain import hub
from langchain_openai import ChatOpenAI
from composio_langchain import ComposioToolSet, App
from decompose_query import decompose_query_into_subqueries
from sub_query import get_subquery_tool
from config import MULTI_HOP_QUERY_MESSAGE
from typing import List
import os
from loguru import logger
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

def process_mulit_hop_query(query: str, available_apps: List[str], context: str = "") -> None:
    
    composio_toolset = ComposioToolSet()

    tools = composio_toolset.get_tools(apps=available_apps)

    sub_queries = decompose_query_into_subqueries(query, available_apps)

    sub_queries_with_tools = []
    for sub_query in sub_queries:
        tool = get_subquery_tool(sub_query, available_apps, context)
        sub_queries_with_tools.append({"sub_query": sub_query, "tool": tool})

    sub_query_and_tool = ""
    for i, sub_query_with_tool in enumerate(sub_queries_with_tools):
        sub_query_and_tool += f"{i}- {sub_query_with_tool['sub_query']}:\n with tool: {sub_query_with_tool['tool']}.\n"

    logger.debug(f"Sub-queries with tools: {sub_query_and_tool}")

    prompt = hub.pull("hwchase17/openai-functions-agent")
    agent = create_openai_functions_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    task = MULTI_HOP_QUERY_MESSAGE.format(
        task=query,
        sub_queries_and_tools=sub_query_and_tool,
        context=context
    )

    agent_executor.invoke({"input": task})


if __name__ == "__main__":
    query = "Star the repo composio on GitHub and mail the contributors"
    from routeApps import route_apps
    available_apps = route_apps(query)
    result = process_mulit_hop_query(query, available_apps)
    logger.info(result)
