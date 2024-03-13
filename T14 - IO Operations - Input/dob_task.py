"""
This program reads the data from the DOB text file and prints it out in two
different sections.
"""

# Creating all necessary variables for future use
container_for_name = ""
container_for_birthdates = ""
file_conten_list = []
path_to_file = "DOB.txt"

# Creating the try-except block to catch "IOError"
try:
    # Opening file in read mode and encoding as 'utf-8'
    with open(path_to_file, 'r', encoding='utf-8') as DOB_file:
        file_conten_list = DOB_file.readlines()

        # Iterating over each line in the `file_conten_list` and splitting each
        # line into a list of words using the `split()` method to have access
        # to each word separately
        for line in file_conten_list:
            line_to_list = line.split()

            # Using the ".join" method to create a string with name and surname
            # and then concatenating it to the previously created container
            # for names
            each_name = " ".join(line_to_list[0:2])
            container_for_name += f"{each_name}\n"

            each_birthday = " ".join(line_to_list[2:len(line_to_list)])
            container_for_birthdates += f"{each_birthday}\n"

        # The code `print(f"\033[1mName\033[0m\n{conteiner_for_name}")` and
        # `print(f"\033[1mBirthday\033[0m\n{conteiner_for_birthdates}")` is used
        # to print the headers "Name" and "Birthday" in bold format.
        print(f"\033[1mName\033[0m\n{container_for_name}")
        print(f"\033[1mBirthday\033[0m\n{container_for_birthdates}")
except IOError as e:
    print(f"Error from file: {e}")
