import os
from bot.chatbot import create_chatbot

def main():
    qa = create_chatbot()
    print("Chatbot is ready. Type 'quit' to exit.")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "quit":
            break
        response = qa.invoke({"question": user_input})
        print("Bot:", response["answer"])

if __name__ == "__main__":
    main()
