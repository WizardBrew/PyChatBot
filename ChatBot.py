# All below modules needed for any help plz conatct Wizardbrew84@gmail.com / Insta = warrior8004
from datetime import date, datetime         # To display time and date
import subprocess as sp                     # To call tasks of system this module needed
import webbrowser as wb                     # To call online sites in browser.
from help import *                          # This is the module toget chat list and help for user.

TimeMod = datetime.now()                    # Variable defined fortime attribute below three/
CurrentTime = TimeMod.strftime("%H:%M:%S")
date_2dy = datetime.now().date()

User_input = ""                             # Valiable to use later as input.

Greet = "Hello i am Chat AI, "                                # Variable to start Chatbot Greeting
Greet_Wishes = "-- I have low Config working in basic mode, Nice to see you,--"   
Greet2 = " = How can i help you =\n"                                   # same above
Var_One = "My name is {User_input}\n, "                         # Not used for now ---- Can use for further Dev'----

def User_input_Function():                                      # Start up function of chatbot
    global UserID
    UserID = input("Enter your name Here: \n\n")                # Asks for user input (to define Name of user)
    print(f"{Greet}\n{Greet_Wishes}\n{Greet2}\n === { UserID} ===,\n")       # dispalys all greet func with user name

User_input_Function()
#=============================================

def validate_Input(UserIp):                                 # User Validation func     
    try:                                                    # Error Handling statement.
        User_input.lower()                                  # whatever user input is taken it will convert to lowercase.
        Switch = {                                          # Since there is no Switch used in python Dictionry is used.
            0 : "I am good Sir, How about you" ,            # chat Answers as Values. of dictionary. 
            1 : f"Your Name is === { UserID } ===\n" ,               # chat Answers as Values. of dictionary. 
            2 : "From Py,Cloud Generated Prog World of WizardBrew",
            3 : "I provide Assistance to chat",
            4 : "Well, Do you beleive in recarnation, bcz i have version",
            5 : "Thats Me, Haha Wait Ofcourse i am kidding. it was in 1964 with name CDC 6600",
            6 : "The Babbage invented, A powerful device that make your task easy like magic for more google",
            7 : f"=== {Greet} ===\nYou can Rename from option below\nhelp or --h",
            8 : "Python is a software programming language by Guido Rossum",
            9 : f"The time is {CurrentTime} and date {date_2dy} ",
            10: " Add your own statements xyz",
            
            39: "Greetings, good to see you",
            40: "Sorry, I am too Young & still Studying, ill get back to you mean while use #- help / --h -# to know about me"         
                }

        if "how" in User_input and "you" in User_input: 
            print(Switch[0])
        elif "what" in User_input and "is my" in User_input and "name" in User_input:
            print(Switch[1])
        elif "where" in User_input and "from" in User_input: 
            print(Switch[2])
        elif "what" in User_input and "do" in User_input:
            print(Switch[3])
        elif "where" in User_input and "birth" in User_input or "birthday" in User_input:
            print(Switch[4])
        elif "what" in User_input and "computer" in User_input and "super" in User_input:
            print(Switch[5])
        elif "who" in User_input and "computer" in User_input and "invented" in User_input:
            print(Switch[6])
        elif "what" in User_input and "is your" in User_input and "name" in User_input:
            print(Switch[7])
        elif "who" in User_input and "python" in User_input or "programing" in User_input:
            print(Switch[8])
        elif "time" in User_input or "date" in User_input or "today" in User_input:
            print(Switch[9])

                 #----=== Add as many as you want. all Parameters as above same  ===----#

                    #----===----=== Tasks Defined ===----===----#   
        elif "open chrome" in User_input or "chrome browser" in User_input or "open browser" in User_input:
            sp.call("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        elif "open control" in User_input or "control panel" in User_input or "c panel" in User_input:
            sp.Popen('C:\\Windows\\System32\\Control.exe')  #----=== Replace your System Path ===----#
        elif "open calculator" in User_input or "calc" in User_input or "calculator" in User_input:
            sp.Popen('C:\\Windows\\System32\\calc.exe')     #----=== Replace your System Path ===----#
        elif "open paint" in User_input or "paint" in User_input or "ms paint" in User_input:
            sp.Popen('C:\\Windows\\System32\\mspaint.exe')  #----=== Replace your System Path ===----#
            
                #_____------------_____Online Tasks_____----------______ 
        elif "open youtube" in User_input or "youtube.com" in User_input or "browse youtube" in User_input:
            wb.register('chrome', None)
            wb.open('https://www.youtube.com')  #----=== Replace your URL's ===----#
        elif "open google" in User_input or "google.com" in User_input or "browse google" in User_input:
            wb.register('chrome', None)
            wb.open('https://www.google.com')   #----=== Replace your URL's ===----#
        elif "open stack" in User_input or "stackoverflow.com" in User_input or "stack overflow" in User_input:
            wb.register('chrome', None)
            wb.open('https://stackoverflow.com/')   #----=== Replace your URL's ===----#
        
            #----=== Add as many as you want. all task as above same  ===----#

        elif "how" in User_input and "you" in User_input or "hi" in User_input or "hello" in User_input: 
            print(Switch[39])       #----=== Do not change this Greet  ===----#
        elif "help" in User_input or "--h" in User_input:
            print(help)             #----=== Do not change this Greet  ===----#
        elif "qw" in User_input or "quit chat" in User_input or "exit" in User_input:
            print("Thank You Sir!! Hope i serverd Info")
        else:
            print(Switch[40])

        
    except:
        print("You must have enter something strange try by typing --h or --help ")
        sp.call(help.txt)

# validate_Input()
#=======================================================================
while User_input != "qw":
    User_input = input("Enter Your Question Here\n\n")
    validate_Input(User_input)






