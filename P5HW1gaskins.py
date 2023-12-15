"""
CTI 110
P5HW1 - Math Quiz
gaskinsl 
11.12.23
"""


import random

def add_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(f" {num1} ") 
    print (f"+{num2}")

    guesses = 0  # Initialize guesses counter
    while True:
        user_answer = int(input("Enter your answer: "))
        guesses += 1  # Increment guesses counter
  
      
        if user_answer == (num1 + num2):
            print("Congratulation!!! Your answer is correct.") 
            print (f"Number of guesses: {guesses}")
            break
        elif user_answer > (num1 + num2):
            print("Sorry, guess is too high.")
        elif user_answer < (num1 + num2):
            print("Sorry, guess is too low.")
            

def subtract_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(f" {num1}")
    print (f"-{num2}")

    guesses = 0  # Initialize guesses counter
    while True:
        user_answer = int(input("Enter your answer: "))
        guesses += 1  # Increment guesses counter
        if user_answer == (num1 - num2):
            print("Congratualtions!!! Your answer is correct.") 
            print (f"Number of guesses: {guesses}")
            break
        elif user_answer > (num1 - num2):
            print("Sorry, guess is too high.")
        elif user_answer < (num1 - num2):
            print("Sorry, guess is too low.")
        else:
            user_answer = int(input("Try again: "))
            

while True:
    print("\nMain Menu:")
    print("1. Add numbers")
    print("2. Subtract numbers")
    print("3. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_numbers()
    elif choice == 2:
        subtract_numbers()
    elif choice == 3:
        print ("Goodbye")
        break
    else:
        print("Invalid choice. Try again.")
