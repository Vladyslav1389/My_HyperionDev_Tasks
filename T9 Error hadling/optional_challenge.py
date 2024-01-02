# How many days have you already lived
# how_old_are_you_now = input("Please when you born in view dd.mm.yy")


condition_for_while = True
while condition_for_while:
    try:
        current_time = input("Please enter current time in the format:'hours(24):minutes'")
        sliced_current_time = current_time.split(':')
        print(f"time_now is : {sliced_current_time}")
        if sliced_current_time < 0 and sliced_current_time[0] > 24:
            Print("error in if statement")


        # tarrget_time = input("Please enter target time in the format: 'hours(24):minutes'")
    except:
        print("Sorry, you entered incorrect number of hours please reapet.")
    else:
        print("Entered date is valid.")
        condition_for_while = False


sliced_target_time = tarrget_time.split(':')
print(f"target_time is : {sliced_target_time}")


hours = (24 - int(sliced_current_time[0])) + int(sliced_target_time[0])
print(f"hours : {hours}")
if hours > 24:
    hours = hours - 24
    print(f"hours in if: {hours}")

minutes = (60 - int(sliced_current_time[1])) + int(sliced_target_time[1])
print(f"minutes : {minutes}")
if minutes > 60:
    minutes = minutes - 60
    print(f"minutes in if: {minutes}")
    hours += 1

total_minutes = hours * 60 + minutes
print(f"Minutes left to target is: {total_minutes}")
