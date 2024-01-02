"""
1. Create a variable that stores user's input.
2. Write if, elif, else statements to separate different conditions.
"""

# Creating an integer variable that stores user's age
user_age = int(input("Please enter your name : "))

# Writing each condition by the if-elif-else statement
if user_age == 21:
    print("Congrats on your 21st!")
elif user_age > 100:
    print("Sorry, you're dead.")
elif user_age >= 65:
    print("Enjoy your retirement!")
elif user_age >= 40:
    print("You're over the hill.")
elif user_age < 0:
    print("You are not born yet!!!")
elif user_age < 13:
    print("You qualify for the kiddie discount.")
else:
    print("Age is but a number.")
