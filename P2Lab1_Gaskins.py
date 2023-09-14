""" 
CTI 110
P2LAB1 - Gas Prices 
Gaskins
9/7/23

Write a program with a car's gas milage (miles/gallon) and the cost of gas (dollars/gallon) as floating-point input, and output the gas cost for 20 miles, 75 miles, and 500 miles.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}')

"""

# ask for miles per gallo 
miles_per_gallon = float (input("What's the car's MPG? "))
# ask for price per gallon of gas
price_per_gallon = float(input("Price per gallon? "))
# show the price per mile to drive
# unit we what is $/miles
price_per_mile = price_per_gallon / miles_per_gallon 
# print("This vehicle costs $",price_per_mile, "to drive 1 mile.")
# f strings are llike this: {variable:.2f} for 2 decimal places 
print(f"This vehicle costs ${price_per_mile:.2f}, to drive 1 mile.")

#Last step: Tell the user the cost to drive 20, 75,and 500 miles

#per 20 miles 
price_per_20miles = price_per_mile*20
print(f"This vehicle costs ${price_per_20miles:.2f}, to drive 20 miles.")
#per 75 miles 
price_per_75miles = price_per_mile*75
print(f"This vehicle costs ${price_per_75miles:.2f}, to drive 75 miles.")
#per 500 miles 
price_per_500miles = price_per_mile*500
print(f"This vehicle costs ${price_per_500miles:.2f}, to drive 500 miles.")


