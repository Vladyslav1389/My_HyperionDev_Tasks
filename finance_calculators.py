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
    user_decision = input("Enter either 'investment' or 'bond' from the menu above"
                      " to proceed: ").lower().strip(' ')
print("check passed")
# =============================================================================
if user_decision == "investment":
    deposit_amount = int(input("Please enter the amount of money that you are depositing: "))
    while deposit_amount <= 0:
        print("You entered negative number or 0. Please enter positive number.")
        deposit_amount = int(input("Please enter the amount of money that you are depositing: "))

    annual_interest_rate = int(input("Please enter the interest rate without the percent sign(%): "))
    while annual_interest_rate < 0:
        print("You entered negative number or 0. Please enter positive number.")
        annual_interest_rate = int(input("Please enter the interest rate without the percent sign(%): "))
# ============================================================================
    amount_of_months = int(input("Please enter the number of years you plan on investment: "))
    while amount_of_months <= 0:
        print("You entered negative number or 0. Please enter positive number.")
        amount_of_months = int(input("Please enter the number of years you plan on investment: "))
# =============================================================================
    interest = input("Enter either 'simple' or 'compound' from the menu above"
                      " to proceed: ").lower().strip(' ')
    while (interest == "simple" or  interest == "compound") != True:
        print("Sorry you entered something wrong. Please, try again.")
        interest = input("Enter either 'simple' or 'compound' from the menu above"
                      " to proceed: ").lower().strip(' ')
# =============================================================================
    if interest == "simple":
        total_amount = deposit_amount * (1 + (annual_interest_rate/100) * amount_of_months)
        #print(f"You will earn: {total_amount}")    
    elif interest == "compound":
        total_amount = deposit_amount * math.pow((1 + (annual_interest_rate/100)), amount_of_months)
    else:
        print("Else")
    print(f"You will get at the end: {total_amount}")

# ======== If user choose "bond" ====================================
elif user_decision == "bond":
    house_value = int(input("Please enter the present value of your house: "))
    while house_value <= 0:
        print("You entered negative number or 0. Please enter positive number.")
        house_value = int(input("Please enter the present value of your house: "))
    
    annual_interest_rate = int(input("Please enter the interest rate without the percent sign(%): "))
    while annual_interest_rate < 0:
        print("You entered negative number or 0. Please enter positive number.")
        annual_interest_rate = int(input("Please enter the interest rate without the percent sign(%): "))
    interest_rate = ((annual_interest_rate) / 100) / 12
    amount_of_months = int(input("Please enter the number of months over which the bond will be repaid: "))
    while amount_of_months <= 0:
        print("You entered negative number or 0. Please enter positive number.")
        amount_of_months = int(input("Please enter the number of months over which the bond will be repaid: "))

    repayment = (interest_rate * house_value)/(1 - math.pow((1 + interest_rate), (-amount_of_months)))
    boot_repayment = (interest_rate * house_value)/(1 - (1 + interest_rate)**(-amount_of_months))
print(f"Amount of money you will have to repay each month is : {repayment}")    


# print(f"check passed again: {interest}")
# print(deposit_amount)
# print(interest_rate)
# print(amount_of_months)
print(f" repayment : {repayment}")
print(f" boot_repayment : {boot_repayment}")
# else:
#     print("Bad")

    