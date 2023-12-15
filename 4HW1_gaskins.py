"""
CTI 110
P4HW1 - Score List 
Gaskins L
10.25.23

This program will first create a loop to enter all the grades. Second, do input validation to make sure all the grades are between 0 and 100.

"""
# variables 
num_scores =0
score = 0
total = 0
score_list = []

# intro
#print("Welcome to the Score Calculator!")

# loop to enter scores
num_scores = int(input("How many scores do you want to enter? " ))
for score_count in range(num_scores):
    print ("Enter score #",score_count +1,": ", end="")
    score = float(input())
    
    
    while score < 0 or score > 100:
      print()
      print("INVALID Score entered!!!! Please enter a score between 0 and 100.")
      print ("Enter score #",score_count +1,": ", end="")
      score = float(input())  
     
    total = total + score
    # add the score to the list
    score_list.append(score)
  
# Calculations
average = total / num_scores
      
#letter grade conversion 
letter_grade = "error"
if  average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
    
      
print()
print ("--------------Results--------------")


print ("Lowest Score : ", min(score_list))
print ("Modified List: ",  score_list)
print ("Average Score: ", average )
print ("Grade        : ", letter_grade)
print ("----------------------------------")

    
        
