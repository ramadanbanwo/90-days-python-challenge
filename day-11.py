import re

def validate_email(email):
    # Define the regular expression for a valid email address
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match to check if the email matches the regex
    if re.match(email_regex, email):
        return True
    else:
        return False

# Collect user input
email = input("Enter an email address to validate: ")

# Validate the email address
if validate_email(email):
    print("The email address is valid.")
else:
    print("The email address is invalid.")