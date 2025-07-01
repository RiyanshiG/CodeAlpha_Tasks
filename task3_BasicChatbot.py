def chatbot():
    print("Bot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi"]:
            print("Bot: Hi there!")
        elif user_input in ["how are you", "how are you?"]:
            print("Bot: I'm fine, thanks.")
        elif user_input in ["bye", "goodbye"]:
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: I'm not sure how to respond to that.")

chatbot()
