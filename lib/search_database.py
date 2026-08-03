from langchain.tools import tool

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
    # For demonstration purposes, we will return a static weather report.
    # In a real implementation, you would call a weather API here.
    return f"The weather in {city} is sunny with a temperature of 25°C and humidity of 60%."

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
