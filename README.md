# 🤖 ChatBot – Rule-Based Terminal Bot by Palak

A friendly, rule-based chatbot built in Python for terminal interaction.  
Designed to simulate simple conversations using pattern recognition and conditional logic.

Developed to practice Python programming, logic design, and basic NLP using `if-else`, `input()`, and emojis for expressive feedback.

---

## 📌 Features

- 🎨 Stylish emoji-based responses in the terminal
- 💬 Rule-based interaction using keywords and logic
- 🤗 Handles greetings, questions like "how are you", and farewells
- 🚪 Graceful exit with words like `bye`, `exit`, or `quit`
- ⚙️ Easy to run in any terminal environment

---

## 🖼️ Demo Screenshot


![chatbot](https://github.com/user-attachments/assets/0e60136b-f670-4ca5-895c-16cb30d87a61)


## 🚀 Getting Started

### 🔧 Requirements
- Python 3.x installed on your system

---

Run the Bot :
Say hi, hello, or namaste
Ask how are you?
Type bye, exit, or quit to end the chat

📁 Project Structure
File	Description
chatbot.py	                         Main chatbot logic
chat_history.txt	                   Auto-generated (optional) chat log
README.md	                           This documentation


🙋‍♀️ Author
Made with 💬 by Palak
🔗 Connect on LinkedIn

⭐ Feedback & Support
If you like this project, consider giving it a ⭐ on GitHub.
Feel free to contribute ideas or enhancements through pull requests.

code: 
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
