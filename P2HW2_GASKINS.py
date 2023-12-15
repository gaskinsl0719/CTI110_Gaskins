# CTI-110
   # P2HW2 - List
   # Latasha Gaskins
   # 9/24/23
   #

 #program to calculate statistics from student test scores

#ask user to enter grades for the following tests
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

#combine grades in a single list 
grade_list = [grade1, grade2, grade3, grade4, grade5, grade6]
print()
print("------------Results------------")

#find max, min, sum, and avg
lowest_grade = min(grade_list)
highest_grade = max(grade_list)
sum_grade = sum(grade_list)
avg_grade = sum_grade / len(grade_list)
                
print(f"Lowest Grade: {lowest_grade}")
print(f"Highest Grade: {highest_grade}")
print(f"Sum of Grades: {sum_grade}")
print(f"Average: {avg_grade:.2f}")
print("----------------------------------------")