import sys
import time
from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from lib.search_database import search_database, get_city_weather


class ChatAgent:
    def __init__(self):
        self.llm = ChatOllama(model="qwen2.5:3b-instruct", keep_alive="30m")
        self.tools = [search_database, get_city_weather]
        self.agent = create_agent(model=self.llm, tools=self.tools)


def main():
    # sys.stdout.reconfigure(encoding="utf-8")
    start_time = time.perf_counter()
    print("Welcome to the Search Agent!")
    chat_agent = ChatAgent()
    result = chat_agent.agent.invoke({"messages": [HumanMessage(content="Get the weather for 'New York' and search the database for 'Document 2'")]})
    print(f"Agent response: {result['messages'][-1].content}")

    elapsed_time = time.perf_counter() - start_time
    print(f"Execution time: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
