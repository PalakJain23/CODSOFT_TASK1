import datetime
import random

def chatbot():
    print("🤖 Chatbot: Hello! I'm PalakBot. Ask me anything or type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if user_input in ["bye", "exit", "quit"]:
            print("🤖 Chatbot: Goodbye! Have a great day! 👋")
            break

        # Greetings
        elif user_input in ["hi", "hello", "hey"]:
            greetings = ["Hello!", "Hey there!", "Hi! How can I help you?", "Namaste!"]
            print("🤖 Chatbot:", random.choice(greetings))

        # How are you?
        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm doing great, thanks for asking! How about you?")

        # What's your name?
        elif "your name" in user_input:
            print("🤖 Chatbot: I'm PalakBot, your rule-based assistant!")

        # Thank you
        elif "thank" in user_input:
            print("🤖 Chatbot: You're welcome! 😊")

        # Date
        elif "date" in user_input:
            today = datetime.date.today()
            print("🤖 Chatbot: Today's date is", today.strftime("%B %d, %Y"))

        # Time
        elif "time" in user_input:
            now = datetime.datetime.now()
            print("🤖 Chatbot: Current time is", now.strftime("%I:%M %p"))

        # Joke
        elif "joke" in user_input:
            jokes = [
                "Why don’t scientists trust atoms? Because they make up everything!",
                "Why did the computer catch a cold? Because it left its Windows open!",
                "Why do programmers prefer dark mode? Because light attracts bugs."
            ]
            print("🤖 Chatbot:", random.choice(jokes))

        # Weather (dummy answer)
        elif "weather" in user_input:
            print("🤖 Chatbot: I'm not connected to the internet, but I hope it's sunny 🌞 where you are!")

        # Simple calculator
        elif "calculate" in user_input:
            print("🤖 Chatbot: Sure! Enter a math expression like 5 + 3")
            try:
                expression = input("🧮 Expression: ")
                result = eval(expression)
                print("🤖 Chatbot: The answer is", result)
            except:
                print("🤖 Chatbot: Oops! That didn't work. Make sure you enter a valid expression.")

        # About Palak
        elif "palak" in user_input:
            print("🤖 Chatbot: Palak is my amazing creator! She's learning AI & building cool things like me!")

        # Fallback
        else:
            print("🤖 Chatbot: Hmm... I didn't understand that. Can you ask something else?")

# Run the chatbot
chatbot()
