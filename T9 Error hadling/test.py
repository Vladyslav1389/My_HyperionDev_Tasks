condition_for_while_block = True
while condition_for_while_block:
    try:
        # current_time = "0.0"
      #  current_time = input("Please enter current time in the format:'hours(24):minutes'")
       # sliced_current_time = current_time.split(':')
       # print(f"time_now is : {sliced_current_time}")
       # print(f"sliced_current_time = {int(sliced_current_time[0])}")
       # print(type(int(sliced_current_time[0])))
        condition_for_nested_while_in_try_block = True
        while condition_for_nested_while_in_try_block:
            current_time = input("Please enter current time in the format:'hours(24):minutes'")
            sliced_current_time = current_time.split(':')
            if int(sliced_current_time[0]) < 0 or int(sliced_current_time[0]) > 23 or int(sliced_current_time[1]) < 0 or int(sliced_current_time[1]) > 59: # if user enter 24 it will be a logical error
                # tarrget_time = input("Please enter target time in the format: 'hours(24):minutes'")
                print("Sorry, you entered incorrect current time, Please repeat.")
            else:
                condition_for_nested_while_in_try_block = False
    except ValueError:
        print("You entered something except colon(':')! Please enter valid format.")
    else:
        print("Check is passed. Data format is valid. Thank you!")
        condition_for_while_block = False


# # How many days have you already lived
# # how_old_are_you_now = input("Please when you born in view dd.mm.yy")

# # Current time
# current_time_while_block = True
# while current_time_while_block:
#     try:
#         current_time_nested_while_in_try_block = True
#         while current_time_nested_while_in_try_block:
#             current_time = input("Please enter current time in the format:'hours(24):minutes'")
#             sliced_current_time = current_time.split(':')
#             if int(sliced_current_time[0]) < 0 or int(sliced_current_time[0]) > 23 or int(sliced_current_time[1]) < 0 or int(sliced_current_time[1]) > 59: # if user enter 24 it will be a logical error
#                 # target_time = input("Please enter target time in the format: 'hours(24):minutes'")
#                 print("Sorry, you entered incorrect current time, Please repeat.")
#             else:
#                 current_time_nested_while_in_try_block = False
#     except ValueError:
#         print("You entered something except colon(':')! Please enter valid format.")
#     else:
#         print("Check is passed. Current data format is valid. Thank you!")
#         current_time_while_block = False

# # Target time
# target_time_while_block = True
# while target_time_while_block:
#     try:
#         target_time_nested_while_in_try_block = True
#         while target_time_nested_while_in_try_block:
#             target_time = input("Please enter target time in the format: "
#                                 "'hours(24):minutes'")
#             sliced_target_time = target_time.split(':')
#             if int(sliced_target_time[0]) < 0 or int(sliced_target_time[0]) > 23 or int(sliced_target_time[1]) < 0 or int(sliced_target_time[1]) > 59: # if user enter 24 it will be a logical error
#                 print("Sorry, you entered incorrect target time, Please repeat.")
#             else:
#                 target_time_nested_while_in_try_block = False
#     except ValueError:
#         print("You entered something except colon(':')! Please enter valid format.")
#     else:
#         print("Check is passed. Target data format is valid. Thank you!")
#         target_time_while_block = False

# # Formulas
# hours = (24 - int(sliced_current_time[0])) + int(sliced_target_time[0])
# print(f"hours : {hours}")
# if hours > 24:
#     hours = hours - 24
#     print(f"hours in if: {hours}")
# print(f"hours : {hours}")

# minutes = (60 - int(sliced_current_time[1])) + int(sliced_target_time[1])
# print(f"minutes : {minutes}")
# if minutes >= 60:
#     minutes = minutes - 60
#     print(f"minutes in if: {minutes}")
#     hours += 1
# print(f"minutes : {minutes}")
# print(f"hours : {hours}")

# total_minutes = hours * 60 + minutes
# print(f"Minutes left to target is: {total_minutes}")

