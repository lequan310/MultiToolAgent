from langchain_community.tools.pubmed.tool import PubmedQueryRun
from langchain_core.tools import tool


# You must use this tool after using the get_intent_tool if the intent is science.
@tool
async def pubmed_tool(query: str) -> str:
    """
    This tool searches for information related to science, healthcare, and medicine on PubMed.

    Args:
        query: the information you want to search for on PubMed.
    """
    tool = PubmedQueryRun()
    result = await tool.ainvoke(query)

    return result
