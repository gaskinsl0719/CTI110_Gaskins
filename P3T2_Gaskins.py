"""

CTI 110 
P3T2 - Choices and Menus
Latasha Gaskins
9/26/23

"""
# The most simple program, with main()
def main():
   #call another function, just use the name with ()
   #my_function()
  print("-"*10, "Main Menu", "-"*10)
  print("1. Order Breakfast")
  print("2. Order Lunch")
  print("3. Order Dinner")

  #Let the user choose
  print ("Your choice?", end="")
  choice = int(input())
  print ("You choose:" , choice)
        
  #branch (if) on choice 
  if choice ==1:
    option_1()
  elif choice ==2:
    option_2()
  elif choice ==3:
    option_3()
  else :
    print("Sorry, that's not an option.")
    
def option_1():
  print("Ordering Breakfast")
  print ("Would you like pancakes or waffles?")
  breakfast_food = input()
  if breakfast_food == "pancakes":
    print("Pancakes, coming up!")
  elif breakfast_food == "waffles":
    print ("Waffles, coming up!")
  else:
    print ("We don't have any", breakfast_food)

def option_2():
  print("Ordering Lunch")
  print("Would you like pizza or salad?")
  lunch_food = input()
  if lunch_food == "pizza":
    print ("That will be 10 mins")
  elif lunch_food == "salad":
    print ("One salad, coming up")
  else:
    print ("We don't have any", lunch_food)
    
def option_3():
  print ("Ordering Dinner")
  print ("Would you like chicken or steak?")
  dinner_food = input()
  if dinner_food == "chicken":
    print ("The Chicken is fantastic!")
  elif dinner_food == "steak":
    print("Great choice! The Steak is very juicy!")
  else:
    print ("We don't have any", dinner_food)
  
 
def my_function():
   print ("This is my function.")
 
# start the program
main()