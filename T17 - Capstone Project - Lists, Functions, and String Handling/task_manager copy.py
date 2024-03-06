# Notes:
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date
# from All_done_functions import *
curr_date = datetime.now()


DATETIME_STRING_FORMAT = "%Y-%m-%d"
path_user_txt = "user.txt"
path_tasks_txt = "tasks.txt"
path_task_overview_txt = "task_overview.txt"
path_user_overview_txt = "user_overview.txt"

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
def validate_username(message):

    user_input = input(message).strip()

    if user_input == "":
        print("Sorry, but you inputed nothing.")
        return validate_username(message)
    else:
        return user_input
##===========================================================================
def display_menu(curr_user):
    if curr_user == 'admin':
        menu = validate_username('''Select one of the following Options below:
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
        menu = validate_username('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: ''').lower()
        return menu
##===========================================================================
def reg_user(username_password):
    '''Add a new user to the user.txt file'''
    # - Request input of a new username
    new_username = validate_username("New Username: ")
    if new_username in username_password.keys():
        print("The user with this name is already exist. Please could you input another user name")
        return reg_user(username_password)

    while True:
        # - Request input of a new password
        new_password = validate_username("New Password: ")

        # - Request input of password confirmation.
        confirm_password = validate_username("Confirm Password: ")

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
    task_username = validate_username("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return add_task(task_list, username_password)
    task_title = validate_username("Title of Task: ")
    task_description = validate_username("Description of Task: ")
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
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
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
    user_tasks = []
    for t in task_list:
        if t['username'] == curr_user:
            disp_str = f"Task ID: \t {t['task_ID']}\n"
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Complete? \t {"Yes" if t['completed'] is True else "No"}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
            user_tasks.append(t['task_ID'])

    user_task_choice = ''
    while user_task_choice != '-1':
        print('-'*79)
        message_task_choice = ("Please enter either: \n"
                               "a specific task (by entering Task ID number)\n"
                               "‘-1’ to return to the main menu\n: ")
        user_task_choice = validate_username(message_task_choice)
        print('-'*79)
        if user_task_choice in user_tasks:
            message_mark_or_edit = ("Please enter:\n"
            "'m' - if you would like to mark the task as complete\n"
            "'e' - if you would like to edit the task\n: ")
            mark_or_edit_choice = validate_username(message_mark_or_edit)
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
def create_exist_file(path_tasks_txt):
    if not os.path.exists(path_tasks_txt):
        with open(path_tasks_txt, 'w') as default_file:
            pass
##===========================================================================
##===========================================================================
def change_username(username_password, user_task_choice, task_list):
    print('-'*79)
    print(f"All usernames of people: ", end='')
    print(', '.join(username_password.keys()))
    while True:
        new_assigned_user = validate_username("Please enter the name of the person"
                                        " to whom you want to assign the task to: ")
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
        edit_task_choice = validate_username(display_choices)

        if edit_task_choice == 'n':
            change_username(username_password, user_task_choice, task_list)

        if edit_task_choice == 'd':
            task_list[int(user_task_choice) - 1]['due_date'] = date_validation()
            write_tasks_to_file(task_list, path_tasks_txt)
    else:
        print("This task is already completed.")
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
def overdue(uncompleted_overdue):
    counter = 0
    for task in uncompleted_overdue:
        if task['due_date'] <= curr_date:
            counter += 1
    return counter
##===========================================================================
def task_overview_report(task_list):
    total_num_tasks = len(task_list)
    completed_tasks = completed_task(task_list)
    uncompleted_tasks = uncompleted_task(task_list)
    uncompleted_overdue = uncompleted_overdue_tasks(task_list)
    percent_uncompleted_tasks = round((uncompleted_tasks * 100) / total_num_tasks)
    percent_overdue_tasks = round((overdue(uncompleted_overdue) * 100) / uncompleted_tasks)
    with open(path_task_overview_txt, 'w') as task_overview_file:
        content = f"The total number of tasks is:~`{total_num_tasks}\n"
        content += f"The total number of completed tasks is:~`{completed_tasks}\n"
        content += f"The total number of uncompleted tasks is:~`{uncompleted_tasks}\n"
        content += f"The total number of uncompleted and overdue tasks is:~`{len(uncompleted_overdue)}\n"
        content += f"The percentage of tasks that are incomplete:~`{percent_uncompleted_tasks}%\n"
        content += f"The percentage of tasks that are overdue is:~`{percent_overdue_tasks}%"
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
    total_users_num = len(user_task)
    total_num_tasks = len(task_list)
    users_list = [user for user in user_task.keys()]

    print('_'*79)
    with open(path_user_overview_txt, 'w') as task_overview_file:
        content = f"The total number of registered users is:~`{total_users_num}\n"
        content += f"The total number of tasks is:~`{total_num_tasks}\n"
        for user in users_list:
            percent_of_tasks = round((len(user_task[user]) * 100) / total_num_tasks)
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
            percent_uncompleted_overdue_tasks = round(len(uncompleted_overdue_tasks(user_task[user])) * 100 / uncompleted)

            content += f"\n\t{user}\n"
            content += f"The total number of assigned tasks to the user:~`{len(user_task[user])}\n"
            content += f"The percentage of the total number of tasks that have been assigned to the user:~`{percent_of_tasks}%\n"
            content += f"The percentage of the tasks assigned to the user that have been completed:~`{percent_of_completed}%\n"
            content += f"The percentage of the tasks assigned to the user that must still be completed:~`{percent_of_uncompleted}%\n"
            content += f"The percentage of the tasks assigned to the user that has not yet been completed and are overdue:~`{percent_uncompleted_overdue_tasks}%\n"
        edited_data = align_to_left(content)

        task_overview_file.write(edited_data)
    print("The reports were generated successfully.")
    return edited_data
##===========================================================================
def total_amount_of_user_task(task_list, username_password):
    users_list = [user for user in username_password.keys()]
    g = {}
    s = {}
    for user in username_password.keys():
        counter = 0
        t = []
        for task in task_list:
            if user == task['username']:
                counter += 1
                t.append(task)
            g[user] = counter
            s[user] = t
    return s


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
    curr_t['due_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[5], DATETIME_STRING_FORMAT)
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
##===========================================================================
    elif menu == 'ds' and curr_user == 'admin':
        print(task_overview_report(task_list))
        print(user_overview_report(task_list, username_password))

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
