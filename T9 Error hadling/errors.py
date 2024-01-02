# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# No parentheses in the print function. Syntax error
print ("Welcome to the error program")

# Here is needless indentation and no parentheses. These are syntax errors
print ("\n")

    # Variables declaring the user's age, casting the str to an int, and printing the result
    # In this block we have needless indentations. Syntax error
age_Str = "24" # Unnecessary one equal sign. Runtime error. Should be without
# " years old" string to be able to do the cast in the next line. Logical error
age = int(age_Str) # It is not possible to convert a string with alphabetic
# characters to an integer variable. Runtime error
print("I'm " + str(age) + " years old.") # Concatenation in print function can be
# done only with string type variables here age variable is an integer. Runtime
# error. No spaces before and after the variable. Logical error

    # Variables declaring additional years and printing the total years of age
    # In this block we have needless indentations. Syntax error
years_from_now = "3" # Will be better to pass an integer value into this variable. Logical error
total_years = age + int(years_from_now) # "years_from_now" should be cast to an
# integer variable because it can't be added an integer to the string. Runtime error

print("In three years I'll be " + str(total_years))# No parentheses. Syntax
# error. No space between two strings. Logical error. "answer_years" should not
# be string type and should be the "total_years" variable cast to an integer
# type. Logical error. Should be printed "In three years I'll be " it will make
# more sense. Logical error

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = (total_years*12) + 6 # variable "total" does not exist, maybe
# meant "total_years" variable. In the first case is a runtime error, in the
# second case logical error. Should be added "6" to match task condition. Logical error

print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")
# No parentheses. Syntax error. "total_months" variable should be cast to the
# string type variable. Runtime error.

#HINT, 330 months is the correct answer
