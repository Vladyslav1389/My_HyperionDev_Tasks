"""
This is a program that allows a user to register students for an exam venue.
"""

path_to_reg_form = 'reg_form.txt'

# The `while True:` loop keeps asking the user for input until a valid input is
# provided by checking if it is an integer.
while True:
    amount_of_students = input("Please enter how many students are"
                               " registering: ")
    if amount_of_students.isnumeric():
        amount_of_students = int(amount_of_students)
        break
    else:
        print("Please use numbers only!")


# Looping entered amount of times this block adds the student's ID and line of
# dots for each iteration.
for student in range(amount_of_students):
    student_id = input(f"Please enter the student's ID number {student + 1}: ")

    with open(path_to_reg_form, 'a', encoding='utf-8') as reg_form_object:
        reg_form_object.write(f"{student_id}" + "." * (79-len(student_id)))
        reg_form_object.write("\n")
