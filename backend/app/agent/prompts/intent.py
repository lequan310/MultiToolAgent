# from langchain_core.prompts import PromptTemplate

# intent_prompt = PromptTemplate.from_template(
#     """
#     <s> [INST] You are an assistant that label the user's message into one of the following categories:

#     labels = {
#         "youtube/video", "science", "facts"
#     }

#     If the message does not clearly fall into youtube/video or science, classify it as facts.

#     Your response must contain only the label of the question: {user_message}
#     <label>

#     [/INST] </s>
#     """
# )
