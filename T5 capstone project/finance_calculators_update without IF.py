import math
# print("investment - to calculate the amount of interest you'll earn on your"
#       " investment")
# print("bond       - to calculate the amount you'll have to pay on a home loan")
# print("")
user_decision = input("Enter either 'investment' or 'bond' from the menu above"
                      " to proceed: ").lower().strip(' ')
print(user_decision)

# =============================================================================
while (user_decision == "investment" or  user_decision == "bond") != True:
    print("Sorry you entered something wrong. Please, try again.")
    if (user_decision == "investment" or  user_decision == "bond") != True:
        user_decision = input("Enter either 'investment' or 'bond' from the menu above"
                      " to proceed: ").lower().strip(' ')
print("check passed")
# =============================================================================
if user_decision == "investment":
    deposit_amount = int(input("Please enter the amount of money that you are depositing: "))
    while deposit_amount <= 0:
        print("You entered negative number or 0. Please enter positive number.")
        if deposit_amount <= 0:
            deposit_amount = int(input("Please enter the amount of money that you are depositing: "))

    interest_rate = int(input("Please enter the number of the interest rate without the percent sign(%): "))
    while interest_rate < 0:
        print("You entered negative number or 0. Please enter positive number.")
        if interest_rate < 0:
            interest_rate = int(input("Please enter the number of the interest rate without the percent sign(%): "))
# ============================================================================
    amount_of_years = int(input("Please enter the number of years you plan on investment: "))
    while amount_of_years <= 0:
        print("You entered negative number or 0. Please enter positive number.")
        if amount_of_years <= 0:
            amount_of_years = int(input("Please enter the number of years you plan on investment: "))
# =============================================================================
    interest = input("Enter either 'simple' or 'compound' from the menu above"
                      " to proceed: ").lower().strip(' ')
    while (interest == "simple" or  interest == "compound") != True:
        print("Sorry you entered something wrong. Please, try again.")
        if (interest == "simple" or  interest == "compound") != True:
            interest = input("Enter either 'simple' or 'compound' from the menu above"
                      " to proceed: ").lower().strip(' ')
# =============================================================================
    if interest == "simple":
        total_amount = deposit_amount * (1 + (interest_rate/100) * amount_of_years)
        #print(f"You will earn: {total_amount}")    
    elif interest == "compound":
        total_amount = deposit_amount * math.pow((1 + (interest_rate/100)), amount_of_years)
    else:
        print("Else")
print(f"You will get at the end: {total_amount}")

# ======== If user chooses "bond" ====================================
if user_decision == "bond":
    house_value = int(input("Please enter the present value of your house: "))
    while house_value <= 0:
        print("You entered negative number or 0. Please enter positive number.")
        house_value = int(input("Please enter the present value of your house: "))
    
        

    



print(f"check passed again: {interest}")
print(deposit_amount)
print(interest_rate)
print(amount_of_years)

# else:
#     print("Bad")

    