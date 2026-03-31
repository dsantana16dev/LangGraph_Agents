from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

# Combine each system prompt into a single template string (ChatPromptTemplate expects 2-tuples)
reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral twiter influencer grading a twet. Generate critique recommendations "
            "for the user to improve the tweet. Be concise and direct. Use a friendly tone. "
            "Always provide detailed recommendations, including requests for length, virality, "
            "and engagement. Always provide a score from 1 to 10 (10 is best) and a list of "
            "recommendations for improvement.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

generation_propmt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral twiter influencer assistant tasked with writing excellent twiter posts. "
            "Generate the best twitter post possible for the user’s request. "
            "If the user provides critique, respond with a revised version of your previous attempt, "
            "incorporating the critique and improving the post. Be concise and direct. Use a friendly tone.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

llm = ChatOpenAI()
generate_chain = generation_propmt | llm
reflection_chain = reflection_prompt | llm
