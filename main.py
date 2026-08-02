import sys
import time
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
load_dotenv()

def main():
    sys.stdout.reconfigure(encoding="utf-8")
    start_time = time.perf_counter()
    print("Hello from langchain-course!")
    # llm = ChatOllama(model="qwen2.5:3b-instruct", keep_alive="30m", reasoning=False, num_ctx=2048)
    llm = ChatOllama(model="qwen2.5:3b-instruct", keep_alive="30m")
    # response = llm.invoke("Hello AI")
    # generate a information data for LLM about Elon Musk in a multi-line variable below called information
    # add some more details in this below variable about Elon Musk's achievements, companies, and contributions to technology and space exploration.
    # split this in multiple lines for better readability and to avoid long lines in the code.

    information = """
    Elon Musk is a billionaire entrepreneur, inventor, and engineer known for his work in the technology and space industries. He was born on June 28, 1971, in Pretoria, South Africa. Musk is the founder, CEO, and chief engineer of SpaceX, a private aerospace manufacturer and space transportation company. 
    He is also the CEO and product architect of Tesla, Inc., an electric vehicle and clean energy company. Musk has been instrumental in advancing electric vehicle technology and promoting sustainable energy solutions.
    """
    # update a dummy person name profile in this below variable called information with more details about their achievements, companies, and contributions to technology and space exploration.
    information = """
    Mr. Govind Fufal is a fictional character used to demonstrate the capabilities of the language model. He is a software engineer and researcher with a focus on artificial intelligence and machine learning.
    """

    summary_template = """
given the information {information} about a person I want to create:
1. A brief summary of the person's achievements and contributions to technology and space exploration.
2. Two interesting facts about them
3. At the end of the response, write this person full name
Ensure that person name is to be picked from the {information} provided and not hardcoded. The response should be concise, informative, and engaging.
    """
    summary_prompt_template = PromptTemplate(
        # regardless of whether you passed the argument yourself. In fact, even if you did pass input_variables=["information"]
        # input_variables=["information"],
        # builds the template, auto-detects it needs information
        template=summary_template,
    )

    # summary_prompt = summary_prompt_template.format(information=information)
    # response = llm.invoke(summary_prompt)
    # here we are using Langchain expression language the pipe operator.
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})

    elapsed_time = time.perf_counter() - start_time
    print(response.content)
    print(f"Execution time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
