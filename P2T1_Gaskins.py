import matplotlib.pyplot as plt

# Collect the data 
data = [] #empty list
"""
print("Enter Pokeman Data:")
print("Day 1: ", end="")
day1 = int(input())
print("Day 2: ", end="")
day2 = int(input())
print("Day 3: ", end="")
day3 = int(input())
"""

# New version - loop and get each day at a time
num_day = int(input("How many days? "))
for day in range (num_day):
  print ("Day ", day, ":", end="")
  today = int(input())
  data.append(today) #add to the end of the list 
  
#put the data in a list (Done)


#do not do total and average yet 
#max and min value in the list 
print ("Best Day:", max(data))
print("Worst Day:", min(data))

#todo Graph real data
fig, ax = plt.subplots()
ax.plot(range(num_day), data)
plt.title ("Pokeman Data")
plt.xlabel('day #')
plt.ylabel('pokemans collected')
plt.show()



