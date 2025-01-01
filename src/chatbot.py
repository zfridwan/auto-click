import re
import random

def chatbot_response(user_input):
    responses = {
        r"hello|hi|hey": [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! Need any assistance?"
        ],
        r"how are you": [
            "I'm just a bot, but I'm doing fine. How about you?",
            "I'm here to assist you! How can I help?"
        ],
        r"what is your name": [
            "I'm your friendly chatbot!",
            "You can call me Chatbot AI."
        ],
        r"bye|goodbye": [
            "Goodbye! Have a great day!",
            "See you later! Take care."
        ]
    }

    for pattern, res_list in responses.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(res_list)

    return "I'm not sure how to respond to that. Can you rephrase?"

def main():
    print("Chatbot AI: Hello! Type 'bye' to end the chat.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("Chatbot AI: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot AI: {response}")

if __name__ == "__main__":
    main()
