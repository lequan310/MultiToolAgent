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
system_prompt = "You are an efficient agent. Answer questions as short as possible."
workflow = create_react_agent(
    llm, tools=tools, checkpointer=memory, state_modifier=system_prompt
)


def get_response_from_stream(message: str):
    config = {"configurable": {"thread_id": "1"}, "recursion_limit": 6}
    input = {"messages": message}
    output = []

    for chunk in workflow.stream(input=input, config=config, stream_mode="values"):
        # Print to track the response
        message = chunk["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

        # Get the content of the response
        content = message.content
        output.append(content)

    return output[-1]


def get_agent_response(message: str):
    response = get_response_from_stream(message)

    return response
