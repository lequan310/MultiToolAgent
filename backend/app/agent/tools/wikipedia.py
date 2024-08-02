from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool


@tool
async def wikipedia_tool(query: str) -> str:
    """
    Search for information about people, places, companies, facts, etc. that you don't know on Wikipedia.
    Prioritize to use this before using search_tool from Tavily unless its about recent or real-time events.

    Args:
        query: the information you want to search for on Wikipedia.
    """
    tool = WikipediaQueryRun(
        api_wrapper=WikipediaAPIWrapper(doc_content_chars_max=1000)
    )
    result = await tool.ainvoke(query)

    return result
