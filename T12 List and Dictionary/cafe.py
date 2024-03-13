"""
The program counts the cafe's total stock worth. 
"""

# Entering all data
menu = ["Tea", "Beer", "Cider", "Coffe"]
stock = {'Tea': 13, 'Beer': 50, 'Cider': 33, 'Coffe': 56}
price = {'Tea': 3.50, 'Beer': 5.90, 'Cider': 5.30, 'Coffe': 4.10}

# Creating a variable in which will be calculated total stock worth
total_stock = 0

# Itereting through the menu list and using each of its items as a key in the
# dictionaries and calculating the total stock worth
for item in menu:
    each_item_value = stock[item] * price[item]
    total_stock += each_item_value
print(f"The total stock worth in the cafe is {total_stock} pounds")
