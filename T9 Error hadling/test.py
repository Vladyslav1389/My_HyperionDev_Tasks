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
