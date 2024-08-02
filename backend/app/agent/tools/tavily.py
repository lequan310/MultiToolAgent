from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool


@tool
async def search_tool(query: str) -> str:
    """
    Search from online sources for newest news, updates, facts, etc. that you don't know from trusthworthy sources.
    The search result is always accurate and up-to-date. Use this tool if you can't find the information on Wikipedia.

    Args:
        query: the information you want to search online.
    """
    tool = TavilySearchResults(max_results=3)
    result = await tool.ainvoke(query)

    return result
