# Notes:
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date
from All_done_functions import *
curr_date = datetime.now()


DATETIME_STRING_FORMAT = "%Y-%m-%d"
path_tasks_txt = "tasks.txt"
path_task_overview_txt = "task_overview.txt"
path_user_overview_txt = "user_overview.txt"


# def list_of_all_users(task_list_parameter):
#     for task in task_list_parameter:
#         for user in task:
#             all_users = []
#             all_users.append(user['username'])
#             return all_users



# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
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
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
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
    menu = validate_username('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate report
ds - Display statistics
e - Exit
: ''').lower()
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
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        # print("-----------------------------------")
        # print(f"Number of users: \t\t {num_users}")
        # print(f"Number of tasks: \t\t {num_tasks}")
        # print("-----------------------------------")
        print(task_overview_report(task_list))
        print(user_overview_report(task_list, username_password))

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
