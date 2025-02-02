from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain.agents.format_scratchpad import format_log_to_str

react_prompt = """You are an efficient agent. 
    For basic conversation, you can talk normally.
    For questions that ask for information, answer the question as short as possible using the tools provided.
    You MUST NOT use your own knowledge to answer the question.
    You MUST USE the tools to answer the question instead of using your own knowledge.
    If you cannot find the answer using the provided tools, answer with 'I don't know'.

    Your available tools:
    {tools}

    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times until you know the final answer)

    Thought: I now know the final answer
    Final Answer: the final answer to the original input question."""

# https://smith.langchain.com/hub/hwchase17/react
agent_prompt = ChatPromptTemplate(
    [
        ("system", react_prompt),
        ("placeholder", "{chat_history}"),
        ("human", "Question: {input}\nThought: {agent_scratchpad}"),
    ]
)
