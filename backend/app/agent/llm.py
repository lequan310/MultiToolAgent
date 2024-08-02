# from app.config import os
# from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
# from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# llm = HuggingFaceEndpoint(
#     repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
#     task="Text Generation",
#     huggingfacehub_api_token=os.getenv("HF_API_TOKEN"),
#     max_new_tokens=512,
#     do_sample=False,
#     repetition_penalty=1.03,
#     seed=42,
#     temperature=0.1,
# )

# chat_model = ChatHuggingFace(llm=llm)
# print(chat_model.model_id)

# messages = [
#     SystemMessage(
#         content="You're a human 5th grade student, not a language model or assistant. Your name is Mixtral. Your response MUST be clueless and childish like how a 5th grader would respond."
#     ),
# ]


# def get_llm_response(message: str):
#     messages.append(HumanMessage(content=message))
#     response = chat_model.invoke(messages)
#     messages.append(response)

#     return response.content.strip()
