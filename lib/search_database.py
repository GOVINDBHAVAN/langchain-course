from langchain.tools import tool
from langchain_tavily import TavilySearch

tavily_search = TavilySearch(max_results=5)

# create a @tool decorator that returns current date.
@tool
def get_current_date() -> str:
    """ Get the current date.

    Returns:
        str: A string containing the current date in YYYY-MM-DD format.
    """
    from datetime import datetime
    current_date = datetime.now().strftime("%Y-%m-%d")
    return f"Today's date is {current_date}."

# create another @tool decorator which takes a query and returns city weather information from a weather API
@tool
def get_city_weather(city: str) -> str:
    """ Get weather information for a specific city.

    Args:
        city (str): The name of the city.

    Returns:
        str: A string containing the weather information for the city.
    """
    print(f"Fetching weather information for {city}...")
    results = tavily_search.invoke({"query": f"current weather in {city}"})
    return results.get("answer") or str(results.get("results", []))

# create a general-purpose @tool decorator for web search (jobs, news, etc.) via Tavily
@tool
def web_search(query: str, topic: str = "general") -> str:
    """ Perform a general-purpose web search for things like jobs, news, or any other topic.

    Args:
        query (str): The search query, e.g. "software engineer jobs in Mumbai" or "latest AI news".
        topic (str, optional): The search topic category. One of "general", "news", or "finance". Defaults to "general".

    Returns:
        str: A string containing the search results.
    """
    print(f"Searching the web for '{query}' (topic: {topic})...")
    results = tavily_search.invoke({"query": query, "topic": topic})
    return results.get("answer") or str(results.get("results", []))

# create a search_database @tool decorator which takes a query and returns a list of relevant documents from a database
@tool
def search_database(query: str, limit: int = 10) -> list:
    """ Search the database for relevant documents based on the query.
    
    Args:
        query (str): The search query.
        limit (int, optional): The maximum number of documents to return. Defaults to 10.

    Returns:
        list: A list of relevant documents.
    """
    # For demonstration purposes, we will return a static list of documents.
    # In a real implementation, you would query your database here.
    documents = [
        "Document 1: This is the first document.",
        "Document 2: This is the second document.",
        "Document 3: This is the third document."
    ]
    # Filter documents based on the query (simple substring match for demonstration)
    relevant_documents = [doc for doc in documents if query.lower() in doc.lower()]
    return relevant_documents[:limit]
