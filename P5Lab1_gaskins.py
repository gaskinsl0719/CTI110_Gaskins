# CTI 110
# P5LAB1 - CYOA
# gaskinsl
# 10.26.23

from choices import *
# first function: main_menu().


def main_menu():
    print("Main Menu")
    print("You're in front of a spooky old house...")
    print("Do you:")
    print("1. Try the front door")
    print("2. Sneak around back")
    print("3. Forget it and go home")
    print("4. [Quit]")
    choice = input("Choose: ")
    if choice == '1':
        choice_front_door()
    elif choice == '2':
        # Call choice 2 here (You can add the corresponding function)
        choice_back_door()
    elif choice == '3':
        # Call choice 3 here (You can add the corresponding function)
        choice_go_home()
    elif choice == '4':
        print("Ok, quitting game")
        return
    else:
        print("That's not a valid choice, please try again.")
        main_menu()

# now we have the choice functions. Feel free to add more.
def choice_front_door():
    print("Try the front door.")
    print("It's locked.")
    print("Do you:")
    print("1. Check around back")
    print("2. Give up and go home")
    choice = input("Choose: ")
    if choice == '1':
        choice_back_door()
    elif choice == '2':
        choice_go_home()
    else:
        print("You have to choose...")
        choice_front_door()

def choice_back_door():
    print("You go to the back of the house.")
    print ("You see a garden shed an a freshly dug grave.")
    choice = choice_menu ("Check out the shed", "Look at the grave")
    if choice == "1": #shed
      print ("Inside the shed is a chainsaw. And a charming man with the chainsaw. Oops")
      print ("*** GAME OVER***")
    elif choice =="2": #grave
      print ("You fall in the grave!... Oh no! ")
      print("You find the key")
      print ("You wander back around front")
      choice_front_door()
def choice_go_home():
  print("You go home.")
  print("You hear a noise coming from the kitchen.")
  print("Do you:")
  print("1. Explore the kitchen")
  print("2. Forget it and go to bed")
  choice = input("Choose: ")
  if choice == '1':
    
    print ("A monster jumps out and eats you!")
    # Call choice 2 here (You can add the corresponding function)
  elif choice == '2':
    
    print("You win!!")

# finally, we have main -- which we use to start the program 
def main():
    print("M5LAB1 - Choose Your Own Adventure")
    main_menu()
    print("Thanks for playing!")

#start the program
main()
