"""
CTI 110
P1HW1- Variables
Gaskins
9//5/23

Do some basic output with numbers
1. ask for an int
2. square it and then cube it 
3. ask for another int 
4. add them and multiply them

"""
#PART ONE: INTEGERS
#variables, first and second
first = 0
second = 0

print ("Enter integer:")
first = int(input()) #take input, then covert it to int
print (first, "squared is", first * first)
print("and", first, "cubed is", first * first * first, "!!")

#get anohter int
print("Enter another integer:")
second = int(input())

print(first,"+",second, "is", first + second)
print(first,"*" ,second, "is", first * second)

#PART TWO: MOVIES
#Three vaiables
#int - the year of the movie
#float - the gross (in million dollars)
#string - a quote
name = "The Super Mario Bros. Movie"
year = 2023
gross = 1.36 # bil $


#Print out this information
#Then print movie quote

print("One of the highest grossing movies of", year, "is", name,"!")
print("It's grossed $", gross, "billion (so far)!") 
print("I'm sure everyone knows Mario's most famous quote:","It's a me, Mario!")