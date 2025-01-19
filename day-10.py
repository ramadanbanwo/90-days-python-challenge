import math #import the math library

user_input = input("Enter the number you want to fin the square rot of: ") #collect user's input and convert it to a string 
#check if the user's input is an integer
try:
    number = int(user_input)
    #perform the square root operation
    result = math.sqrt(number)
    #print the result
    print(f"The square root of {number} is {result}")
except ValueError:
    print(f"sorry, wrong input.")
