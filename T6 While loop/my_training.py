# # correct_input = -1
# # total_amount = 0
# # counter = 0
# # user_input = 0
# # user_input = int(input("Please enter a number :"))
# # while user_input == correct_input:
# #     print(print("Your average of the numbers entered, excluding the -1 "
# #       f"is :{average_amount}"))

# """Average of the numbers entered by user before they entered '-1'"""

# # Variable stores the number that a user should enter to stop the program
# correct_input = -3
# # Variable will store the total sum of the numbers entered
# total_amount = 0

# # Variable will store the number of inputs
# counter = 0

# user_input = 0

# # Checking if a user will enter correct
# # if user_input == correct_input:
# #     print(f"Your average of the numbers entered is :{correct_input}")
# # else:
# while user_input != correct_input:
#     user_input = int(input("Please enter a number :"))
#     total_amount += user_input
#     counter += 1
#     print(f"counter is :{counter}    total amount is :{total_amount}")


# total_amount_without_last_enter = total_amount - correct_input
# counter_without_last_enter = counter - 1
# if counter_without_last_enter == 0:
#     counter_without_last_enter += 1
#     total_amount_without_last_enter += correct_input
# average_amount = total_amount_without_last_enter / counter_without_last_enter
# print("Your average of the numbers entered, excluding the -1 "
#     f"is :{average_amount}")

var = 3/0
print(var)