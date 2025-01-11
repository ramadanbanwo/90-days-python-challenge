# this is program that takes a number as input and returns the factorial of that number 
number = int(input('What is the number you want to find the factorial of?: '))#take user input
#initialize the result variable
result = 1
#user a for loop to iterate from 1 to the input number (inclusive)
for num in range(1, number + 1):
    #multiply the results by the current number
    result *= num
#print the factorial
print(f'The factorial of {number} is {result}')