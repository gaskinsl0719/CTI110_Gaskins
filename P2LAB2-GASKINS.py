"""

CTI 110 
P2LAB2 - Simple Statistics
Latasha Gaskins
9.23.23

Given 4 floating-point numbers. Use a string formatting expression with conversion specifiers to output their product and their average as integers (rounded), then as floating-point numbers.

Output each rounded integer using the following:
print(f'{your_value:.0f}')
Output each floating-point value with three digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.3f}')

"""
#variables
num1 = float(input("Enter value 1: "))
num2 = float(input("Enter value 2: "))
num3 = float(input("Enter value 3: "))
num4 = float(input("Enter value 4: "))



#output poduct as intergers rounded and as floating-point numbers 
product = num1 * num2 * num3 * num4
print(f"The product is {product:.0f} or {product:.3f}")

#output average as intergers rounded and as floating-point numbers
average = (num1 * num2 * num3 * num4)/ 4
print(f"The average is {average:.0f} or {average:.3f}")
