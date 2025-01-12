name = input("Enter your name: ")
age = int(input("Enter your age: "))
email = input ("Enter your email:")

user_info = {
    'name': name,
    'age': age,
    'email': email
    }

print('would you like to see your information?(yes/no)')
answer = input()
if answer == 'yes':
    print(f"Your name is {user_info['name']}, you are {user_info['age']} years old and your email is {user_info['email']}")
elif answer =='no':
    print("Thank you for your time")
else:
    print("Invalid input")