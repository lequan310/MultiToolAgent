from app.config import os
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools.pubmed.tool import PubmedQueryRun
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import AgentExecutor, create_react_agent
from app.agent.prompts.agent import agent_prompt
from langchain.agents.format_scratchpad import format_log_to_str
from app.agent.tools.pubmed import pubmed_tool
from app.agent.tools.wikipedia import wikipedia_tool
from app.agent.tools.tavily import search_tool
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage, AIMessage
from app.config import os

# from app.agent.tools.get_intent import get_intent

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    huggingfacehub_api_token=os.getenv("HF_API_TOKEN"),
    max_new_tokens=1024,
    repetition_penalty=1.03,
    seed=42,
    temperature=0.1,
    cache=False,
)

chat_model = ChatHuggingFace(llm=llm)
chat_history = []

custom_tools = [pubmed_tool, wikipedia_tool, search_tool]
tools = [
    WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper()),
    PubmedQueryRun(),
    TavilySearchResults(max_results=3),
]

agent = create_react_agent(llm=chat_model, tools=custom_tools, prompt=agent_prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=custom_tools,
    verbose=True,
    handle_parsing_errors=True,
    # return_intermediate_steps=False,
)


async def get_agent_response(message: str):
    response = await agent_executor.ainvoke(
        {"input": message, "chat_history": chat_history}
    )
    cleaned_response = response["output"].strip()

    chat_history.append(HumanMessage(content=message))
    chat_history.append(AIMessage(content=cleaned_response))

    print(cleaned_response)
    return cleaned_response
