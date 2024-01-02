# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # No quotations. Runtime error because it looks for the Lion variable
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"
# Missed up number_of_teeth with animal_type. Runtime error. Should be the 'f'
# character at the start of the variable to use the format function. Runtime error

print(full_spec) # No parentheses. Syntax error
