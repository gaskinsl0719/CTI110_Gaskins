"""
CTI 110 
P3HW1 - Letter Grades
Gaskins L 
9/28/23

Convert a number grade into a letter grade. (Ten point scale)
"""

#Get student grades 
print ("Enter garde 1: ",end="")
grade1 = int(input())
print ("Enter garde 2: ", end="")
grade2 = int(input())
print ("Enter garde 3: ", end="")
grade3 = int(input())
print ("Enter garde 4: ", end="")
grade4 = int(input())
print ("Enter garde 5: ", end="")
grade5 = int(input())

#put grades in a list
my_grades = [grade1, grade2, grade3, grade4, grade5]

#get average of grades 
avg_grade = (grade1 + grade2 + grade3 + grade4 + grade5) / len(my_grades)
print (f"The average grade for this student is {avg_grade:.0f}.")

num_grade = avg_grade

#Get the number grade
letter_grade = "G" #error if G is output 
#Do the conversion
if num_grade >= 90:
  letter_grade = "A"
elif num_grade >= 80:
  letter_grade  = "B"
elif num_grade  >= 70:
  letter_grade = "C"
elif num_grade >= 60:
  letter_grade = "D"
else: 
  letter_grade = "F"


#print the letter grade 
print(f"A grade of {num_grade:.0f} is a", letter_grade)


