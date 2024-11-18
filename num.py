import random

# Predefined responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey! How can I assist you?"],
    "how are you": ["I'm just a program, but I'm functioning as expected! How about you?"],
    "what is your name": ["I'm your friendly chatbot!", "You can call me Chatbot."],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I'm not sure I understand. Can you please rephrase?"]
}

# Chatbot logic
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for better matching
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])  # Pick a random response
    return random.choice(responses["default"])

# Chat loop
print("Chatbot: Hi! I'm here to chat with you. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Chatbot:", random.choice(responses["bye"]))
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
