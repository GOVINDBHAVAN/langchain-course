import sys
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
load_dotenv()

def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("Hello from langchain-course!")
    llm = ChatOllama(model="qwen3:4b")
    response = llm.invoke("Hello AI")
    print(response)

if __name__ == "__main__":
    main()
