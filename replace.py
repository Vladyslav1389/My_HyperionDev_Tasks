example_sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Replacing "!" signs with " " by the .replace() function
example_sentence_without_exlamantion = example_sentence.replace('!', ' ')
print(example_sentence_without_exlamantion.replace('!', ' '))

# Changing the "example_sentence_without_exlamantion_mark" to upper case
# by the .upper() function
example_sentence_in_upper_case = example_sentence_without_exlamantion.upper()
print(example_sentence_in_upper_case.upper())

# Turning the "example_sentence_in_upper_case" around
print(example_sentence_in_upper_case[::-1])