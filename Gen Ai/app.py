from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

model_groq = init_chat_model("groq:llama-3.1-8b-instant")

def generate_topic(topic):
    prompt = f"""
Give information about the topic: {topic}

Use exactly this format:

Definition:
Write a short and simple definition.

Three Key Points:
1.
2.
3.

Real-Life Example:
Give one simple real-life example.
"""

    response = model_groq.invoke(prompt)
    return response.content

topic = input("Enter a topic: ")

result = generate_topic(topic)

print("\n", result)