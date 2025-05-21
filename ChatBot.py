from datetime import datetime
import subprocess as sp
import webbrowser as wb

# Get current time and date
current_time = datetime.now().strftime("%H:%M:%S")
current_date = datetime.now().date()

# Function to get user name at start
def get_user_name():
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}! How can I assist you today?")
    return user_name

user_name = get_user_name()

# Dictionary for chatbot responses
responses = {
    "how are you": "I'm good! How about you?",
    "what is my name": f"Your Name is === {user_name} ===",
    "where from": "From the cloud world of AI!",
    "what do you do": "I provide assistance with chat and system tasks.",
    "time": f"The current time is {current_time} and the date is {current_date}.",
    "exit": "Thank You! Hope I served you well!"
}

# Dictionary for system commands
commands = {
    "open chrome": lambda: sp.call("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"),
    "open calculator": lambda: sp.Popen("C:\\Windows\\System32\\calc.exe"),
    "open google": lambda: wb.open("https://www.google.com")
}

# Function to process user input
def process_input(user_input):
    user_input = user_input.lower().strip()  # Normalize user input
    
    # Check predefined responses
    for key in responses:
        if key in user_input:
            print(responses[key])
            return

    # Check predefined system commands
    for key in commands:
        if key in user_input:
            commands[key]()  # Execute command
            return

    print("Sorry, I didn't understand that. Try asking something else.")

# Chat loop
while True:
    user_input = input("Enter Your Question: ")
    if user_input.lower() == "exit":
        process_input(user_input)
        break
    process_input(user_input)
