"""
Write a program to calculate and displays travel expenses 
9/17/2023
CTI-110 P1HW2 - Travel 
Latasha Gaskins

"""
print ("This program caculates and displays travel expenses.")
print()
#ask user to enter their budget 
user_budget =  int(input("Enter budget: "))   
print()
#ask user to enter travel destination 
user_destination = (input("Enter your travel destination: "))
print()
#ask user for amount they will spend on gas 
user_fuel =  int(input("How much do you think you will spend on gas? "))
print()
#ask user for amount they will spend on accomodation
user_accomodation =  int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
#ask user for amount they will use on food 
user_food = int (input("Last, how much do you need for food? "))
print()
#add expenses 
user_expenses = user_fuel + user_accomodation + user_food
print("------------Travel Expenses------------")
print ("Location:",user_destination)
print (f"Initial Budget: ${user_budget:.1f}")
print(f"Fuel: ${user_fuel:.1f}")
print(f"Accomodation: ${user_accomodation:.1f}")
print(f"Food: ${user_food:.1f}")
print("----------------------------------------")
print()
#subtract expense from budget
user_balance = user_budget - user_expenses
print(f"Remaining Balance: ${user_balance:.1f}")