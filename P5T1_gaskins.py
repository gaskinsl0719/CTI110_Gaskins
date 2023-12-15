#CTI 110
#P5T1 - Function 
#gaskinsl
#10.24.23

def main():
  print("Hello world!")
  burger = 4.999
  print_money(burger)
  print_money (10)
  print_money (.5)
#main() ends 
#other functions go here
def print_money(amount):
  print("$", format(amount,".2f"), sep="")

#Now, start the program
main()

