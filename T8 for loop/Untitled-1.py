"""
This is a program displaying increasing and decreasing asterisks, using just 
one "for" loop and "if-elif" statements.
"""

# Total amount of lines with asterisks
amount_of_lines = 9

# Determine the middle of the range to use in the if-elif statements
# to determine the highest number of asterisks
middle_of_the_range = amount_of_lines / 2

# Counter for the number of asterisks that should be printed in the line
amount_of_asteriskss = 0

# Iterated specific amount of times(amount of lines with asterisks)
for iteration in range(0, amount_of_lines):

    # Iterate up to the middle of the range(up to the biggest amount of
    # asterisk on a line). With each iteration firstly add 1 to the amount of
    # asterisks then print it out by multiplying the asterisk sign by the
    # amount of asterisk
    if iteration < middle_of_the_range:
        amount_of_asteriskss += 1
        print('*' * amount_of_asteriskss)

    # Iterate up to the endest point of the range
    elif iteration > middle_of_the_range:
        amount_of_asteriskss -= 1
        print('*' * amount_of_asteriskss)