"""
This program shows time when a user should take their medicine.
User should take medicine every 4 hours at 3 hours after they got up.
"""

get_up_time = 9
take_period = 4 # medicine taking period
first_take = get_up_time + 3 # time of first medication intake

for iter in range(0, 25): # for each hour in range of 24 hours
    # If time equals to first take do iteration through the range of the day
    # in medicine taking period and print hours that correspond its.
    if iter == first_take:
        last_take = get_up_time + 17 # waking time
        for inner_iter in range(first_take, last_take, take_period):
            if inner_iter <= 24: # cheking that whithin one day
                print(f"Now is {inner_iter} o'clock. It is time to take your "
                  "medicine!")
            else:
                break

"""
Logical mistake is that we used the 'range(0, 25)' instead of 'range(0, 24)'
because it is impossible that clocks shows 24 hours.
"""