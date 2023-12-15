"""

CTI-110
P4HW2 - Salary Calculator
Latasha Gaskins
10.26.23

"""

#variables
total_employees =0
total_overtime = 0 
total_reg_pay = 0
total_gross = 0
keep_going =True

# ask once to start the loop
name = input("Enter employee's name or 'Done' to terminate: ")
while keep_going == True:
  
  
  print("How many hours did",name,"work? ", end="")
  num_hours = float(input())
  print("What is ",name,"'s pay rate? ", sep="",end="")
  pay_rate = float(input())

  #overtime hours evaluation and calculations
  overtime_hours = num_hours - 40

  if num_hours <= 40:
      overtime_hours = 0

  reg_pay = (num_hours - overtime_hours) * pay_rate
  overtime_pay = (overtime_hours * 1.5) * pay_rate
  gross_pay = overtime_pay + reg_pay

  print ()
  print("Employee name: ", name)
  print()
  print(
      "Hours Worked    Pay Rate   OverTime   OverTime Pay    RegHour Pay    Gross Pay"
  )
  print(
      "-------------------------------------------------------------------------------"
  )
  print(f"{num_hours:<15}", f"{pay_rate:<10}", f"{overtime_hours:<12}", end="")
  print(f"{overtime_pay:<15.2f}", f"${reg_pay:<15.2f}", f"${gross_pay:.2f}")
  print()
  # get ready to repeat again, or end
  name = input("Enter employee's name or 'Done' to terminate: ")
  if name == 'Done':
    #exit
    keep_going = False
  total_employees += 1
  total_overtime += overtime_pay
  total_reg_pay += reg_pay
  total_gross += gross_pay
# end of loop
print()
print ("Total number of employees entered: ", total_employees)
print ("Total amount paid for overtime: ", f"${total_overtime:.2f}")
print ("Total amount paid for regular hours: ", f"${total_reg_pay:.2f}")
print ("Total amount paid in gross: ", f"${total_gross:.2f}")





