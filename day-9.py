#this program takes user input and catches an error if the input is invalid
try:
    num = int(input('Enter a number: '))
    result = 10 / num #divides 10 by whatever value the user inputs
except ValueError as val:
    print('Invalid input!!. Please input a number') #prints this error message if the user input isn't an integer 
except ZeroDivisionError:
    print('You cannot divide by zero!!!') #prints this error message if the user's input is zero as it isn't possible to divide by zero
else:
    print(f'the result is {result}') #prints the result of the calculation