"""
1. Ask and store all user's information.
2. Output all gathered information.
"""

# Gathering all user's information and storing it in variables
users_name = input("Please enter your name :")
users_age = input("Please enter your age :")
users_house_number = input("Please enter your house number :")
users_street_name = input("Please enter your street name :")

# Printing whole sentence with all user's information
print(f"""This is {users_name}. He is {users_age} years old and lives at house
number {users_house_number} on {users_street_name}.""")