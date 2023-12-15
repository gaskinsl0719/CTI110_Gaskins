"""

CTI-110
P3HW2 - Salary
Latasha Gaskins
10.08.23

"""
#variables
name = input("Enter employee's name: ")
num_hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))


print("---------------------------------------")

#overtime hours evaluation and calculations
overtime_hours = num_hours - 40

if num_hours<= 40: 
  overtime_hours = 0
  

reg_pay = (num_hours - overtime_hours) * pay_rate 

overtime_pay = (overtime_hours * 1.5) * pay_rate

gross_pay = overtime_pay + reg_pay



print ("Employee name: ", name)
print ()
print ("Hours Worked    Pay Rate   OverTime   OverTime Pay    RegHour Pay    Gross Pay" )
print("-------------------------------------------------------------------------------")
print (f"{num_hours:<15}",        f"{pay_rate:<10}",         f"{overtime_hours:<12}",end="") 
print(f"{overtime_pay:<15.2f}", f"${reg_pay:<15.2f}",f"${gross_pay:.2f}")