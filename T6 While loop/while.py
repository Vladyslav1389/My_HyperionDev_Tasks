"""Average of the numbers entered by a user before they entered '-1'."""

# Variable stores the number that a user should enter to stop the program
correct_input = -1

# Variable will store the total sum of the numbers entered
total_amount = 0

# Variable will store the number of inputs
counter = 0

# This variable is needed for the first comparison in the "while" loop
user_input = 0

# This block of code checks for correspondence input and counting 
#   tries and input numbers
while user_input != correct_input:
    user_input = int(input("Please enter a number :"))
    total_amount += user_input
    counter += 1

# Distracting last input
total_amount_without_last_enter = total_amount - correct_input
counter_without_last_enter = counter - 1

# Checking division by 0 in case of if first input will be correct the counter
#   will be 1 and the counter without the last enter will be 0. Or if correct
#   input changes to a new number for example -2 we will have the same
#   situation when if first input is wrong and the second correct counter
#   without the last enter will be zero again
if counter_without_last_enter == 0:
    counter_without_last_enter += 1

# Counting the average of the entered numbers
average_amount = total_amount_without_last_enter / counter_without_last_enter
print("Your average of the numbers entered, excluding the -1 "
    f"is :{average_amount}")