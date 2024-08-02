# from langchain_core.tools import tool
# from app.agent.prompts.intent import intent_prompt
# from app.agent.llm import llm


# @tool("get_intent_tool")
# def get_intent(message: str) -> str:
#     """You MUST use this tool at the beginning to get the intent of the question or message.
#     This tool helps you get the intent of the message or questions.

#     Args:
#         message: the message or question to get the intent of
#     """

#     intent_prompt.format(user_message=message)
#     response = llm.invoke(intent_prompt)

#     return response
