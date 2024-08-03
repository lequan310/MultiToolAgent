from app.config import os
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools.pubmed.tool import PubmedQueryRun
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from app.agent.tools.pubmed import pubmed_tool
from app.agent.tools.wikipedia import wikipedia_tool
from app.agent.tools.tavily import search_tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from app.config import os

# from app.agent.tools.get_intent import get_intent

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
memory = MemorySaver()

custom_tools = [pubmed_tool, wikipedia_tool, search_tool]
tools = [
    WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper()),
    PubmedQueryRun(),
    TavilySearchResults(max_results=3),
]

workflow = create_react_agent(llm, tools=tools, checkpointer=memory)


def get_agent_response(message: str):
    config = {"configurable": {"thread_id": "1"}}
    input = {"messages": message}

    response = workflow.invoke(input=input, config=config, stream_mode="values")
    response = response["messages"][-1].content
    print(response)
    return response
