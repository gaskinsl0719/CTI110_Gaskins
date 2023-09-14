import matplotlib.pyplot as plt
import turtle

# Collect the data
# New version - loop and get each day at a time
data = [] #empty list
#num_days = int(input("how many days? "))
num_days = turtle.numinput("Input","How many days? ")
num_days = int(num_days)
for day in range (num_days):
  #print ("Day ", day, ":", end="")
  #today = int(input())
  label = "Day #" + str(day) # "Day 1" and so on 
  today = turtle.numinput("Next Day", "How many Pokeman?")
  data.append(today) #add to the end of the list 
  
#put the data in a list (Done)

#max and min value in the list 
print ("Best Day:", max(data))
print("Worst Day:", min(data))
#TO DO: toal and average 
total =0
for num in data:
  total += num
  #total is now all the numbers in data, added up 
average = total /num_days
print("Total:", total)
print ("Average:", average)

#todo Graph real data
fig, ax = plt.subplots()
ax.plot(range(num_days), data)
plt.title ("Pokeman Data")
plt.xlabel('day #')
plt.ylabel('pokemans collected')
plt.show()



