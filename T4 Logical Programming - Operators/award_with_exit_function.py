import sys
"""
1. Request input from a user for each event of the triathlon individually.
2. Store each input in the coresponded event variable.
3. Add minutes all together and store them into their own variable.
4. Spread awards throw participants by using if-elif-else statements based on 
   the final variable.
"""

# Creating 3 variables for each event by requesting input from a user
minutes_for_swimming = int(input("Please enter amount of minutes spent for"
                                 " swimming: "))
while minutes_for_swimming <= 0:
    print("You entered negative number or 0. Please enter positive number")
    if minutes_for_swimming <= 0:
        minutes_for_swimming = int(input("Please enter amount of minutes spent"
                                         " for swimming: "))
    # else:
    #     print("error")
    #     sys.exit()

minutes_for_cycling = int(input("Please enter amount of minutes spent for"
                                 " cycling: "))
minutes_for_running = int(input("Please enter amount of minutes spent for"
                                 " running: "))

# Add all minutes into one variable
total_minutes_for_all_events = (minutes_for_swimming + minutes_for_cycling 
                                + minutes_for_running)
print("Total time taken to complete the triathlon: {} minutes."
      .format(total_minutes_for_all_events))

# Spreading awards based on the total_minutes_for_all_events variable by 
# using if-elif-else statements
if 0 < total_minutes_for_all_events <= 100:
    print("Your award is : \"Provincial Colours\"")
elif 101 <= total_minutes_for_all_events <= 105:
    print("Your award is : \"Provincial Half Colours\"")
elif 106 <= total_minutes_for_all_events <= 110:
    print("Your award is : \"Provincial Scroll\"")
elif total_minutes_for_all_events >= 111:
    print("No award")
elif total_minutes_for_all_events <= 0:
    print("You even didn't participate!")
