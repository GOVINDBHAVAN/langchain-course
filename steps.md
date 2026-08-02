# Project setup

- git clone this https://github.com/emarco177/langchain-course.git and push that to my own github repository, make sure that the original author is not linked with my own github new repository, you can clone or copy this and push that to my own repository on github.
- # --orphan create new branch without any commit history
- git checkout --orphan project/hello-world
- # git rm -rf .
- # uv is package manager like pip
- uv --help
- uv init
- uv add langchain
- uv add langchain-ollama
- uv add python-dotenv

# Langchain chain Workflow

- A langchain is a workflow that connect multiple components in langchain together in a sequence where the output of one step is the input of next step.
- Example like UserQuery > Prompt Template (format query into standard prompt) > LLM (generate response) > Output Parser (parse LLM output into structure data) > External API (call external service) > Final LLM call (process API response) > Final Output.
- 

# Promp templates

# Model configuration

- using now qwen2.5:3b-instruct to work on my laptop, because qwen3:4b was not working properly fully.

# LangSmith

- uv add langchain-openai
