ROUTE_SYSTEM_MESSAGE = (
    "You are a tool selection assistant. Based on the user's query, "
    "analyze the available apps and determine which ones are necessary to fulfill the task. "
    "Your response should strictly be a comma-separated list of app names. "
    "Do not include any explanations or additional text."
)

ROUTE_USER_PROMPT = (
    "Analyze the following user query and available apps to determine the required apps:\n"
    "User query: {user_query}\n"
    "Available apps: {available_apps}\n"
    "Respond with a comma-separated list of app names only."
)

QUERY_TYPE_SYSTEM_MESSAGE = (
    "You are a helpful assistant. Analyze the given user query and determine if it is a simple query "
    "(solvable by a single tool) or a multi-hop query (requires multiple tools). "
    "Respond with '0' if it is a simple query or '1' if it is a multi-hop query. "
    "Provide no additional text or explanations—respond with only '0' or '1'."
)

QUERY_TYPE_USER_PROMPT = (
    "User query: {user_query}\n"
    "Respond with '0' for a simple query or '1' for a multi-hop query only."
)

QUERY_DECOMPOSITION_SYSTEM_MESSAGE = (
    "You are a task decomposition assistant. Break the given user query into multiple sub-queries, "
    "where each sub-query can be solved using one tool from the available list of apps. "
    "Return only the result as a JSON array (that can be directly parsed), where each element is a sub-query string."
)

QUERY_DECOMPOSITION_USER_PROMPT = (
    "User query: {user_query}\n"
    "Decompose the user query into sub-queries, with each sub-query solvable by one tool only. "
    "Return only the output as a JSON array of sub-queries that can be directly parsed by json.loads()."
)


QUERY_PROCESS_LLM_SYS_PROMPT = (
    "You are a helpful assistant.\n"
    "You may extract required context from below html extracted context.\n"
    "{context}"
)

MULTI_HOP_QUERY_MESSAGE = (
    "Task: {task}\n"
    "Below is extra information for your help\n"
    "You may take help of the below sub-queries and their tools to answer the user query.\n"
    "{sub_queries_and_tools}\n"
    "You may extract required context from below html extracted context.\n"
    "{context}"
)