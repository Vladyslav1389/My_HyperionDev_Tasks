import math
""" An investment calculator and a home loan repayment calculator. """

# Printing information for user
print("investment - to calculate the amount of interest you'll earn on your"
      " investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print("")

# =============================================================================
# Creating a choice for a user which calculator they want to use.
# Checking for unwanted spaces by .strip(' ') method.
# Removing all incorrect case input using .lower() method.
# Using "while" loop for repeatedly displaying incorrect input in order to user
#    fix it.
user_decision = input("Enter either 'investment' or 'bond' from the menu above"
                      " to proceed: ").lower().strip(' ')
while (user_decision == "investment" or  user_decision == "bond") != True:
    print("Sorry you entered something wrong. Please, try again.")
    user_decision = input("Enter either 'investment' or 'bond' from the menu "
                      "above to proceed: ").lower().strip(' ')
    
# =============================================================================
# Using "if" statement to determine which calculator we will use.
if user_decision == "investment":
    # Asking the user for the amount of money that they are depositing 
    #   using "input" function and immediately cast it to an integer type.
    deposit_amount = int(input("Please enter the amount of money that you are "
                               "depositing: "))
    # Using "while" loop for repeatedly displaying incorrect input in order to
    #   avoid negative numbers and zeros.
    while deposit_amount <= 0:
        print("You entered negative number or 0. Please enter positive number.")
        deposit_amount = int(input("Please enter the amount of money that you "
                                   "are depositing: "))
    # =========================================================================
    # Asking the user for the interest rate using "input" function and
    #   immediately cast it to an integer type.
    annual_interest_rate = int(input("Please enter the interest rate without "
                                     "the percent sign(%): "))
    while annual_interest_rate < 0:
        print("You entered negative number or 0. Please enter positive number.")
        annual_interest_rate = int(input("Please enter the interest rate "
                                         "without the percent sign(%): "))
    # =========================================================================
    # Asking the user for the number of years they plan on investing using
    #     "input" function and immediately cast it to an integer type.
    amount_of_years = int(input("Please enter the number of years you plan "
                                 "on investment: "))
    while amount_of_years <= 0:
        print("You entered negative number or 0. Please enter positive number.")
        amount_of_years = int(input("Please enter the number of years you "
                                     "plan on investment: "))
    # =========================================================================
    # Using "if" statement to determine which interest user want “simple” or 
    #    “compound” interest.
    interest = input("Enter either 'simple' or 'compound' from the menu above"
                      " to proceed: ").lower().strip(' ')
    while (interest == "simple" or  interest == "compound") != True:
        print("Sorry you entered something wrong. Please, try again.")
        interest = input("Enter either 'simple' or 'compound' from the menu "
                      "above to proceed: ").lower().strip(' ')
    # =========================================================================
    # Using "if-elif" statements to choose which formula should we use.
    if interest == "simple":
        total_amount = deposit_amount * (1 + (annual_interest_rate/100)
                                         * amount_of_years)
    elif interest == "compound":
        total_amount = deposit_amount * math.pow((1 
                       + (annual_interest_rate/100)), amount_of_years)
    # Output the result of calculating.
    print(f"You will get at the end: {total_amount}")

# =============================================================================
# If user choose "bond". Gathering all information that we need for computation.
elif user_decision == "bond":
    house_value = int(input("Please enter the present value of your house: "))
    while house_value <= 0:
        print("You entered negative number or 0. Please enter positive number.")
        house_value = int(input("Please enter the present value of your "
                                "house: "))
# =============================================================================
    annual_interest_rate = int(input("Please enter the interest rate without "
                                     "the percent sign(%): "))
    while annual_interest_rate < 0:
        print("You entered negative number or 0. Please enter positive number.")
        annual_interest_rate = int(input("Please enter the interest rate "
                                         "without the percent sign(%): "))
    interest_rate = ((annual_interest_rate) / 100) / 12
# =============================================================================
    amount_of_months = int(input("Please enter the number of months over "
                                 "which the bond will be repaid: "))
    while amount_of_months <= 0:
        print("You entered negative number or 0. Please enter positive number.")
        amount_of_months = int(input("Please enter the number of months over "
                                     "which the bond will be repaid: "))

    # Calculating how much money the user will have to repay each month by
    # using formula for bond and output the answer.
    repayment = (interest_rate * house_value)/(1 - math.pow((1 
                 + interest_rate), (-amount_of_months)))

    print(f"Amount of money you will have to repay each month is : {repayment}")    
