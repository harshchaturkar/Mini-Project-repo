from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

model_groq = init_chat_model("groq:llama-3.1-8b-instant")

model_mistral = init_chat_model("mistral-small-2603")

while True:
    user = input("\nSelect your model (groq/mistral) or enter quit to exit: ").lower()

    if user == "quit":
        print("\nThank you.")
        break

    elif user == "groq":
        data = input("\nEnter Your Question: ")
        response = model_groq.invoke(data)
        print("\n", response.content)

    elif user == "mistral":
        data = input("\nEnter Your Question: ")
        response = model_mistral.invoke(data)
        print("\n", response.content)

    else:
        print("\nPlease select either 'groq', 'mistral', or 'quit'.")