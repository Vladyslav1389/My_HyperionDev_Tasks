"""
It is a task manager that allows to add users, add tasks, modify tasks( change
the person to whom the task is assigned, change the due date, and mark a task
as completed). Track all tasks and track tasks that are assigned to each
person. It also allows the admin to generate, display and write reports into
a file. 
"""


import os
from datetime import datetime, date


##===========================================================================
def display_menu(curr_user: str) -> str:
    """
    The function `display_menu` presents a menu of options based on the current
    user, allowing them to select various actions.
    
    :param curr_user: The user that logged in.
    :type curr_user: str
    :return: Display menu options based on the user type. If the current user
        is 'admin', the menu includes additional options such as 'gr - Generate
        report' and 'ds - Display statistics'. If the current user is not
        'admin', the menu does not include these additional options. The
        function returns the selected menu option as a lowercase string.
    :rtype: str
    """

    # Checking if the current user is 'admin'. If the current user is 'admin',
    # it will display a menu with additional options: generating a report and
    # displaying statistics.
    if curr_user == 'admin':
        menu = input_validation('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate report
ds - Display statistics
e - Exit
: ''').lower()
        return menu

    else:
        menu = input_validation('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: ''').lower()
        return menu


##===========================================================================
def reg_user(username_password: dict) -> None:
    """
    The function `reg_user` registers a new user by prompting for a username 
    and password, validating the inputs, and storing the user data in a file.
    If the username already exists, the function will recursively call itself
    until a unique username is provided.
    
    :param username_password: is a dictionary that stores usernames as keys and
    passwords as values.
    :type: dict
    :return: None
    """
    
    # The code snippet is attempting to validate a new username input by the
    # user. If the new username already exists in the `username_password`
    # dictionary, it will prompt the user to input another username. The
    # `validate_username` function is expected to handle the validation of the
    # new username. If the username is valid, the code will proceed with the
    # registration process by calling the `reg_user` function.
    new_username = input_validation("New Username: ")
    if new_username in username_password.keys():
        print("The user with this name is already exist. Please could you"
              " input another user name")
        return reg_user(username_password)

    while True:
        # - Request input of a new password
        new_password = input_validation("New Password: ")

        # - Request input of password confirmation.
        confirm_password = input_validation("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password
            
            with open(path_user_txt, "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))
            break
        # - Otherwise you present a relevant message.
        else:
            print("Passwords do no match. Please retry.")


##===========================================================================
def add_task(task_list, username_password):
    '''Allow a user to add a new task to task.txt file
    Prompt a user for the following: 
        - A username of the person whom the task is assigned to,
        - A title of a task,
        - A description of the task and 
        - the due date of the task.'''
    task_username = input_validation("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return add_task(task_list, username_password)
    task_title = input_validation("Title of Task: ")
    task_description = input_validation("Description of Task: ")
    due_date_time = date_validation()


    # Then get the current date.
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        'task_ID': str(len(task_list) + 1),
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    write_tasks_to_file(task_list, path_tasks_txt)

    print("Task successfully added.")
    print('-'*79)
    # print(task_list)
##===========================================================================
def view_all_tasks(task_list):
    '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
    '''

    for t in task_list:
        disp_str = f"Task ID: \t {t['task_ID']}\n"
        disp_str += f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += (f"Date Assigned: \t "
                     f"{t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n")
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Complete? \t {"Yes" if t['completed'] is True else "No"}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)
##===========================================================================
def view_user_task(task_list, curr_user):
    '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
    print(f"All the tasks that have been assigned to {curr_user}:\n")
    user_tasks = []
    for t in task_list:
        if t['username'] == curr_user:
            disp_str = f"Task ID: \t {t['task_ID']}\n"
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += (f"Date Assigned: "
                         f"\t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n")
            disp_str += (f"Due Date: "
                         f"\t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n")
            disp_str += (f"Task Complete? "
                         f" \t{"Yes" if t['completed'] is True else "No"}\n")
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
            user_tasks.append(t['task_ID'])

    user_task_choice = ''
    while user_task_choice != '-1':
        print('-'*79)
        message_task_choice = ("Please enter either: \n"
                               "a specific task (by entering Task ID number)\n"
                               "‘-1’ to return to the main menu\n: ")
        user_task_choice = input_validation(message_task_choice)
        print('-'*79)
        if user_task_choice in user_tasks:
            message_mark_or_edit = ("Please enter:\n"
            "'m' - if you would like to mark the task as complete\n"
            "'e' - if you would like to edit the task\n: ")
            mark_or_edit_choice = input_validation(message_mark_or_edit)
            print('-'*79)
###==========================================================================
            if mark_or_edit_choice == 'm':
                task_list[int(user_task_choice) - 1]['completed'] = True
                user_task_choice = '-1'
                create_exist_file(path_tasks_txt)
                write_tasks_to_file(task_list, path_tasks_txt)
###==========================================================================
            if mark_or_edit_choice == 'e':
                edit_task(user_task_choice, task_list, username_password)
        else:
            print("You entered task that do not assigned to particular user.")
##===========================================================================
def task_overview_report(task_list):
    if len(task_list) == 0:
        return print("Sorry, but you do not have any tasks yet")

    total_num_tasks = len(task_list)
    completed_tasks = completed_task(task_list)
    uncompleted_tasks = uncompleted_task(task_list)
    uncompleted_overdue = uncompleted_overdue_tasks(task_list)
    percent_uncompleted_tasks = round((uncompleted_tasks * 100) / total_num_tasks)
    percent_overdue_tasks = round((overdue(uncompleted_overdue) * 100)
                                   / uncompleted_tasks)
    with open(path_task_overview_txt, 'w') as task_overview_file:
        content = f"The total number of tasks is:~`{total_num_tasks}\n"
        content += f"The total number of completed tasks is:~`{completed_tasks}\n"
        content += (f"The total number of uncompleted tasks"
                    f" is:~`{uncompleted_tasks}\n")
        content += (f"The total number of uncompleted and overdue tasks"
                    f" is:~`{len(uncompleted_overdue)}\n")
        content += (f"The percentage of tasks that are incomplete:~`"
                    f"{percent_uncompleted_tasks}%\n")
        content += (f"The percentage of tasks that are overdue"
                    f" is:~`{percent_overdue_tasks}%")
        edited_data = align_to_left(content)

        task_overview_file.write(edited_data)
    return edited_data
##===========================================================================
def align_to_left(content):
    splited = content.split('\n')
    max_len = len(max(splited, key=len))
    aligned_content = ''
    for line in splited:
        indentation = '_'*((max_len - len(line)) + 3)
        line = line.replace('~`', indentation)
        aligned_content += line + "\n"
    return aligned_content
##===========================================================================
def user_overview_report(task_list, username_password):
    user_task = total_amount_of_user_task(task_list, username_password)
    total_users_num = len([user for user in username_password.keys()])
    total_num_tasks = len(task_list)
    users_list = [user for user in user_task.keys()]

    with open(path_user_overview_txt, 'w') as task_overview_file:
        content = f"The total number of registered users is:~`{total_users_num}\n"
        content += f"The total number of tasks is:~`{total_num_tasks}\n"
        for user in users_list:
            percent_of_tasks = round((len(user_task[user]) * 100)
                                      / total_num_tasks)
            completed = 0
            for task in user_task[user]:
                if task['completed']:
                    completed += 1

            if len(user_task[user]) == 0:
                content += f"\nUser '{user}' does not have a task.\n"
                continue

            percent_of_completed = round(completed * 100 / len(user_task[user]))
            uncompleted = len(user_task[user]) - completed
            percent_of_uncompleted = round(uncompleted * 100 / len(user_task[user]))
            percent_uncompleted_overdue_tasks = round(len
                (uncompleted_overdue_tasks(user_task[user])) * 100 / uncompleted)

            content += f"\n\t{user}\n"
            content += (f"The total number of assigned tasks to the"
                        f" user:~`{len(user_task[user])}\n")
            content += (f"The percentage of the total number of tasks that have"
                        f" been assigned to the user:~`{percent_of_tasks}%\n")
            content += (f"The percentage of the tasks assigned to the user"
                        f" that have been completed:~`{percent_of_completed}%\n")
            content += (f"The percentage of the tasks assigned to the user that"
                        f" must still be completed:~`{percent_of_uncompleted}%\n")
            content += (f"The percentage of the tasks assigned to the user that"
                        f" have not yet been completed and are "
                        f"overdue:~`{percent_uncompleted_overdue_tasks}%\n")
        edited_data = align_to_left(content)

        task_overview_file.write(edited_data)
    return edited_data
##===========================================================================
def total_amount_of_user_task(task_list, username_password):
    divt_users_with_their_tasks = {}
    for user in username_password.keys():
        list__of_particular_user_task = []
        for task in task_list:
            if user == task['username']:
                list__of_particular_user_task.append(task)
            divt_users_with_their_tasks[user] = list__of_particular_user_task
    return divt_users_with_their_tasks
##===========================================================================
def date_validation():
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")
    if due_date_time >= curr_date:
        return due_date_time.date()
    else:
        print("The due date cannot be before the current date.")
        return date_validation()


##===========================================================================
def input_validation(message: str) -> str:
    """
    Removes spaces at the beginning and end of input and also checks for empty
    input recursively prompting a user for valid input.

    :param message: Massage that will display to a user.
    :type message: str
    :return: Validated user input.
    :rtype: str
    """
    # Removes spaces at the beginning and end of input
    user_input = input(message).strip()

    # Checks for empty input recursively prompting a user for valid input
    if user_input == "":
        print("Sorry, but you inputed nothing.")
        return input_validation(message)
    else:
        return user_input
##===========================================================================
def overdue(uncompleted_overdue):
    counter = 0
    for task in uncompleted_overdue:
        if task['due_date'] <= curr_date:
            counter += 1
    return counter
##===========================================================================
def completed_task(task_list):
    completed = 0
    for task in task_list:
        if task['completed']:
            completed += 1
    return completed
##===========================================================================
def uncompleted_task(task_list):
    uncompleted = 0
    for task in task_list:
        if task['completed'] != True:
            uncompleted += 1
    return uncompleted
##===========================================================================
def uncompleted_overdue_tasks(task_list):
    uncompleted_overdue_list =[]
    for task in task_list:
        if task['completed'] == False and task['due_date'] <= curr_date:
            uncompleted_overdue_list.append(task)
    return uncompleted_overdue_list
##===========================================================================
def create_exist_file(path_tasks_txt):
    if not os.path.exists(path_tasks_txt):
        with open(path_tasks_txt, 'w') as default_file:
            pass
##===========================================================================
def change_username(username_password, user_task_choice, task_list):
    print('-'*79)
    print(f"All usernames of people: ", end='')
    print(', '.join(username_password.keys()))
    while True:
        message = ("Please enter the name of the person to whom you want to"
        " assign the task to: ")
        new_assigned_user = input_validation(message)
        if new_assigned_user in username_password.keys():
            task_list[int(user_task_choice) - 1]['username'] = new_assigned_user
            write_tasks_to_file(task_list, path_tasks_txt)
            break
        else:
            print("Unexist person or incorrect person name!")
##===========================================================================
def edit_task(user_task_choice, task_list, username_password):
    if task_list[int(user_task_choice) - 1]['completed'] == False:
        display_choices = ("Please enter:\n"
                           "'n' if you want to change the username of the person"
                           " to whom the task is assigned\n"
                           "'d' if you want to change the due date of the task\n"
                           "any other button to choose another task: ")
        edit_task_choice = input_validation(display_choices)

        if edit_task_choice == 'n':
            change_username(username_password, user_task_choice, task_list)

        if edit_task_choice == 'd':
            task_list[int(user_task_choice) - 1]['due_date'] = date_validation()
            write_tasks_to_file(task_list, path_tasks_txt)
    else:
        print("This task is already completed.")
##===========================================================================
## write to file
def write_tasks_to_file(task_list, path_tasks_txt):

    with open(path_tasks_txt, "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['task_ID'],
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
##===========================================================================
curr_date = datetime.now()
DATETIME_STRING_FORMAT = "%Y-%m-%d"
path_user_txt = "user.txt"
path_tasks_txt = "tasks.txt"
path_task_overview_txt = "task_overview.txt"
path_user_overview_txt = "user_overview.txt"


# Create tasks.txt if it doesn't exist
if not os.path.exists(path_tasks_txt):
    with open(path_tasks_txt, "w") as default_file:
        pass

with open(path_tasks_txt, 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for task_ID, t_str in enumerate(task_data, 1):
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['task_ID'] = str(task_ID)
    curr_t['username'] = task_components[1]
    curr_t['title'] = task_components[2]
    curr_t['description'] = task_components[3]
    curr_t['due_date'] = (datetime.strptime(task_components[4],
                                             DATETIME_STRING_FORMAT))
    curr_t['assigned_date'] = (datetime.strptime(task_components[5], 
                                                 DATETIME_STRING_FORMAT))
    curr_t['completed'] = True if task_components[6] == "Yes" else False

    task_list.append(curr_t)



#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists(path_user_txt):
    with open(path_user_txt, "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open(path_user_txt, 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print('-'*79)
        print("Login Successful!")
        logged_in = True


while True:
    # Presenting the menu to the user and 
    # making sure that the user input is converted to lowercase.
    print()
    print('='*79)
    menu = display_menu(curr_user)
    print('='*79)
##gr - generate reports
##===========================================================================
    if menu == 'r':
        reg_user(username_password)
##===========================================================================
##===========================================================================
    elif menu == 'a':
        add_task(task_list, username_password)
##===========================================================================
##===========================================================================
    elif menu == 'va':
        view_all_tasks(task_list)
##===========================================================================
##===========================================================================
    elif menu == 'vm':
        view_user_task(task_list, curr_user)
##===========================================================================
    elif menu == 'gr' and curr_user == 'admin':
        task_overview_report(task_list)
        user_overview_report(task_list, username_password)
        print("The reports were generated successfully.")
##===========================================================================
    elif menu == 'ds' and curr_user == 'admin':
        print(task_overview_report(task_list))
        print(user_overview_report(task_list, username_password))
        print("The reports were generated successfully.")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
