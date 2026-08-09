import sys
from typing import List
import time
from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from lib.search_database import search_database, get_city_weather, get_current_date, web_search
from pydantic import BaseModel, Field

# Source class inherits from BaseModel.
class Source(BaseModel):
    """Schema for a source used by the agent"""
    # "..." means no default value, and the field is required. The description provides information about the field.
    name: str = Field(..., description="The name of the source.")
    url: str = Field(..., description="The URL of the source.")

# this class we will use to return the agent's response, which includes the answer and a list of sources used by the agent. The sources are represented as a list of Source objects.
class AgentResponse(BaseModel):
    """Schema for the agent's response"""
    answer: str = Field(..., description="The agent's answer to the query.")
    # In python you cannot write = [] as default value (like C# new List<T>()), default_factory takes callable that pydantic alls fresh every-time a new instance of the model is created. This is to avoid mutable default arguments..
    sources: List[Source] = Field(default_factory=list, description="A list of sources used by the agent.")

class ChatAgent:
    def __init__(self):
        self.llm = ChatOllama(model="qwen2.5:3b-instruct", keep_alive="30m")
        self.tools = [search_database, get_city_weather, get_current_date, web_search]
        # self.tools = []
        self.agent = create_agent(model=self.llm, tools=self.tools,response_format=AgentResponse)

def main():
    # sys.stdout.reconfigure(encoding="utf-8")
    start_time = time.perf_counter()
    print("Welcome to the Search Agent!")
    chat_agent = ChatAgent()
    # result = chat_agent.agent.invoke({"messages": [HumanMessage(content="1) Display current date, 2) Today's weather for 'Mumbai', 3) Search the database for 'Document 2', 4) Find the latest AI news, and 5) Find software engineer top 3 job openings in Mumbai")]})
    result = chat_agent.agent.invoke(
        {"messages": [HumanMessage(content="Do a web search for Microsoft, and display it's latest stock price")]})
    # print number of tool calls made by the agent
    tool_call_count = sum(len(getattr(message, "tool_calls", []) or []) for message in result["messages"])
    print(f"Number of tool calls made by the agent: {tool_call_count}")
    # 'structured_response' comes from create_agent's internal graph state added by langchain.
    # since we are using a custom response_format, we can access the structured_response attribute to get the agent's response in our custom format.
    structured_response = result.get("structured_response")
    if structured_response is not None:
        print(f"Agent response: {structured_response.answer}")
        if structured_response.sources:
            # print("Sources:")
            for source in structured_response.sources:
                print(f"  - {source.name}: {source.url}")
    else:
        # Small local models don't always call the structured-output tool;
        # fall back to the last message's plain text in that case.
        print(f"Agent response (unstructured): {result['messages'][-1].content}")

    elapsed_time = time.perf_counter() - start_time
    print(f"Execution time: {elapsed_time:.2f} seconds")

def main2():
    # sys.stdout.reconfigure(encoding="utf-8")
    start_time = time.perf_counter()
    print("Welcome to the Search Agent!")
    chat_agent = ChatAgent()
    # result = chat_agent.agent.invoke({"messages": [HumanMessage(content="1) Display current date, 2) Today's weather for 'Mumbai', 3) Search the database for 'Document 2', 4) Find the latest AI news, and 5) Find software engineer top 3 job openings in Mumbai")]})
    result = chat_agent.agent.invoke(
        {"messages": [HumanMessage(content="1) calculate 2+3, 2) calculate 3+4, 3) calculate 4+5. Do the above calculation and display the results in a list format")]})
    # print number of tool calls made by the agent
    tool_call_count = sum(len(getattr(message, "tool_calls", []) or []) for message in result["messages"])
    print(f"Number of tool calls made by the agent: {tool_call_count}")
    print(f"Agent response: {result['messages'][-1].content}")

    elapsed_time = time.perf_counter() - start_time
    print(f"Execution time: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
