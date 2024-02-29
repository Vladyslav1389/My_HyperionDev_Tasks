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


DATETIME_STRING_FORMAT = "%Y-%m-%d"
path_tasks_txt = "tasks.txt"


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
print(f"task_list={task_list}")


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
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = validate_username('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
ds - Display statistics
e - Exit
: ''').lower()

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
        #         print(f"in the loop : {user_tasks}")
        # print(f"out for loop : {user_tasks}")
        user_task_choice = ''
        while user_task_choice != '-1':
            user_task_choice = validate_username("Please enter either a specific task"
                                 " (by entering Task ID number) or input ‘-1’ to return to the main menu: ")
            if user_task_choice in user_tasks:
                mark_or_edit_choice = validate_username("If you would like to mark the task as complete please enter"
                                            " 'm', if you would like to edit the task please enter 'e': ")
 ###==========================================================================               
                if mark_or_edit_choice == 'm':
                    task_list[int(user_task_choice) - 1]['completed'] = True
                    user_task_choice = '-1'
                    create_exist_file(path_tasks_txt)
                    write_tasks_to_file(task_list, path_tasks_txt)
                    print(f"{task_list[int(user_task_choice) - 1]}")
 ###==========================================================================               
                if mark_or_edit_choice == 'e':
                    edit_task_choice = validate_username("Please enter 'n' if you want to change "
                                                         "the username of the person to whom the task "
                                                         "is assigned\nor 'd' if you want to change the"
                                                         " due date of the task\nor any other button to choose another task: ")
                    
                    if edit_task_choice == 'n':
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
                    
                    if edit_task_choice == 'd':
                        task_list[int(user_task_choice) - 1]['due_date'] = date_validation()
                        write_tasks_to_file(task_list, path_tasks_txt)

            else:
                print("You entered task that do not assigned to particular user.")
                
        print(f"{task_list[int(user_task_choice) - 1]}")

        

        ##
        ## print("Please enter the number of task_ID to edit or enter '-1' to go to the main menu")
        ## user_choice = str(input(^))
        ##

                


##===========================================================================
##===========================================================================
    elif menu == 'ds' and curr_user == 'admin':
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")