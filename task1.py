def chatbot():
    print("Hello! I am your chatbot. Type 'exit' to quit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi there! How can I help you?")
        elif user_input == "how are you?":
            print("Bot: I'm just a bot, but I'm doing great! Thanks for asking.")
        elif user_input == "what is your name?":
            print("Bot: I am a rule-based chatbot.")
        elif user_input in ["bye", "exit"]:
            print("Bot: Goodbye! Have a nice day.")
            break
        else: 
            print("Bot: Sorry, I didn't understand that.")

chatbot()
