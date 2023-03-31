"""
=====================================
Title: Random Password Generator
Author: Micheal LeBlanc
Date: 03/31/2023
=====================================
"""

# Import Libraries
import string #for random password creation
import random #for randomly selecting from ASCII characters
import datetime #as a timestamp of when user/pass was create
import sys

# Global data types
database = []

# Define functions
def core_iteration():
    print("\n******Welcome to the Unsafe Database******")
    print("Select a number from the Main Menu:")
    print("1: Enter username for a password to be assigned.")
    print("2: Lookup a username")
    print("E: Exit the program")
    user_input = input("\nSelection:")

    if user_input == "E" or "e":
        get_user_input(user_input.upper())
    else:
        get_user_input(user_input) 

    #ADD AN INPUT VERIFICATION HERE (I.E. WHAT HAPPENS IF USER ENTERS "Z" OR "14")
def get_user_input(selection):
    match selection:
        case "1":
            get_username()
        case "2":
            return print("lookup a username function") #Define this function
        case "E":
            exit_system()

def exit_system():
    print("Thanks for trusting that your information is safe with Unsafe Database!")
    sys.exit()

def get_username():
    print("Enter a username to be entered into the database.")
    username = input("Username: ")
    print("Username is", username)


# Starts program
core_iteration()

"""
the list is the main storage
each user name will be a key in a dictionary
the password will be assigned as the value for the username creating a key-value pair
"""