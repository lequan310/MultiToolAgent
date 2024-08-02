from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool


@tool
async def search_tool(query: str) -> str:
    """
    Search from online sources for information that you don't know from trusthworthy sources.
    The search result is always accurate and up-to-date.
    Use this tool if you can't find the information with wikipedia_tool.
    For question asking about recent or real-time updates, this tool should be prioritized over wikipedia_tool.

    Args:
        query: the information you want to search online.
    """
    tool = TavilySearchResults(max_results=3)
    result = await tool.ainvoke(query)

    return result
