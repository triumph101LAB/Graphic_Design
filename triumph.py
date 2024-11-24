# My coming Back to Python
import time

def passscode():
    correct_passcode = 1234

    max_attempts = 3

    for attempts in range(max_attempts):
        passcode = int(input("Enter in the passcode: "))
        
        if passcode == correct_passcode:
            print("Correct you Got it Well😁")
        else:
            print("Try Again")
    if passcode != correct_passcode:
        print("Sorry too may attempts") 
