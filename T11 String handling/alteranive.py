"""
This program reads in a string and makes each alternate
character into an upper case character and each other alternate character
a lowercase character.
"""
# Asking a user for input and creating an empty variable to store changed values
first_user_input = input("Please enter your string: ")
altered_string = ""

# Iterrating through each character of the string and changing each even index
# character to upper case else characters changing to lower case
for string_index, each_character in enumerate(first_user_input):
    if string_index == 0 or string_index % 2 == 0:
        character_in_string = each_character.upper()
    else:
        character_in_string = each_character.lower()
    # Adding each changed character into the new string after each iteration
    altered_string += character_in_string
print(altered_string)


# =============================================================================
# This program reads in a string and makes the same string but making each
# alternative word lower and upper case.
# =============================================================================

second_user_input = input("Please enter your string: ")

# Making a list from user input with "split()" method
splited_user_input = second_user_input.split()

# Creating a new empty list to add changed values to it
rearranged_user_input = []

# Using enumerate for loop to get index_word and value(word_in_input).
# index_word is needed to determine which value should be upper or lower
# case by using an if-else statement
for index_word, word_in_input in enumerate(splited_user_input):
    if index_word % 2 == 0:
        changed_word = word_in_input.lower()
    else:
        changed_word = word_in_input.upper()
    
    # Creating a changed list by adding each value that went through iteration
    # to rearranged_user_input list with "append()" method
    rearranged_user_input.append(changed_word)

# Creating new changed string by using "join()" method and printing it
print(' '.join(rearranged_user_input))
