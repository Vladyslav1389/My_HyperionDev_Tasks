# # deposit_amount = int(input("Please enter the amount of money that you are depositing: "))
# # def check(x):

    

# #     while x <= 0:
# #         print("You entered negative number or 0. Please enter positive number.")
# #         if x <= 0:
# #             x #= int(input("Please enter the amount of money that you are depositing: "))

# # # check(deposit_amount)
# # deposit_amount = int(input("Please enter the amount of money that you are depositing: "))
# #     while deposit_amount <= 0:
# #         print("You entered negative number or 0. Please enter positive number.")
# #         if deposit_amount <= 0:
# #             deposit_amount = int(input("Please enter the amount of money that you are depositing: "))

# #     interest_rate = int(input("Please enter the number of the interest rate without the percent sign(%): "))
# #     while interest_rate < 0:
# #         print("You entered negative number or 0. Please enter positive number.")
# #         if interest_rate < 0:
# #             interest_rate = int(input("Please enter the number of the interest rate without the percent sign(%): "))

# #house_value = input("Please enter the present value of your house: ")
# house_value_int = int(input("Please enter the present value of your house: "))
# #print(f"house_value_int  in the start :{house_value_int}, {type(house_value_int)}")
# while house_value_int <= 0:
#     print("You entered negative number or 0. Please enter positive number.")
#     #print(f"house_value_int in the midle :{house_value_int}, {type(house_value_int)}")
#     #if house_value_int <= 0:
#     house_value_int = int(input("Please enter the present value of your house: "))
#         #print(f"house_value_int in if statement :{house_value_int}, {type(house_value_int)}")

# #print(f"house value :{house_value}, {type(house_value)}")
# #print(f"house_value_int in the end :{house_value_int}, {type(house_value_int)}")

# if user_decision == "bond":
house_value = int(input("Please enter the present value of your house: "))
while house_value <= 0:
    print("You entered negative number or 0. Please enter positive number.")
    house_value = int(input("Please enter the present value of your house: "))

print(f"house value is : {house_value}")