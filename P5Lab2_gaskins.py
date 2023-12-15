# CTI110 
#P5Lab2 - Functions 
#gaskinsl
#11/2/23

#First, Print a table of squares 

def main():
  print ("P5LAB2 - Squares")
  print ("number\tnumber squared")
  #range (1, 11) gives numbers 1-10
  for num in range (1, 11):
    num_squared = square (num)
    print_row(num, num_squared)
    
#square () is a value-returning function   
def square(number):
  #input: a number 
  #output: the square of the number
  square = number * number    
  return square 
#print_row() is a void function 
def print_row (num, squared):
  print (num, "\t\t", squared)


if __name__ == "__main__": #only runs the "main" program if there were imports added 
  
  main()