import os
from datetime import datetime, date



DATETIME_STRING_FORMAT = "%Y-%m-%d"
path_tasks_txt = "tasks.txt"

##===========================================================================
def date_validation():
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")
    curr_date = datetime.now()
    if due_date_time.date() >= curr_date.date():
        return due_date_time.date()
    else:
        print("The due date cannot be before the current date.")
        return date_validation()
##===========================================================================
def validate_username(message_parametr):

    user_input = input(message_parametr).strip()

    if user_input == "":
        print("Sorry, but you inputed nothing.")
        return validate_username(message_parametr)
    else:
        return user_input

# message = "Please input the user name: "
# print(validate_username(message))

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
            
            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))
            print(username_password)
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
    curr_date = date.today()
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
    # with open("tasks.txt", "w") as task_file:
    #     task_list_to_write = []
    #     for t in task_list:
    #         str_attrs = [
    #             t['task_ID'],
    #             t['username'],
    #             t['title'],
    #             t['description'],
    #             t['due_date'].strftime(DATETIME_STRING_FORMAT),
    #             t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
    #             "Yes" if t['completed'] else "No"
    #         ]
    #         task_list_to_write.append(";".join(str_attrs))
    #     task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")
    print(task_list)
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
## write to file
def write_tasks_to_file(task_list_paramentr, path_tasks_txt_parametr):

        with open(path_tasks_txt_parametr, "w") as task_file:
            task_list_to_write = []
            for t in task_list_paramentr:
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

def create_exist_file(path_tasks_txt):
        if not os.path.exists(path_tasks_txt):
            with open(path_tasks_txt, 'w') as default_file:
                pass
##===========================================================================
### displaying the users
# def list_of_all_users(task_list_parameter):
#     for task in task_list_parameter:
#         for user in task:
#             all_users = []
#             all_users.append(user['username'])
#             return all_users
##===========================================================================
# def display_user_task(task_list_parameter, curr_user_parameter):
#     user_tasks = []
#     for t in task_list_parameter:
#         if t['username'] == curr_user_parameter:
#             disp_str = f"Task ID: \t {t['task_ID']}\n"
#             disp_str += f"Task: \t\t {t['title']}\n"
#             disp_str += f"Assigned to: \t {t['username']}\n"
#             disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
#             disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
#             disp_str += f"Task Complete? \t {"Yes" if t['completed'] is True else "No"}\n"
#             disp_str += f"Task Description: \n {t['description']}\n"
#             print(disp_str)
#             user_tasks.append(t['task_ID'])
#     return user_tasks
##===========================================================================
def change_username(username_password, user_task_choice, task_list):
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
        display_choices = ("Please enter 'n' if you want to change "
                          "the username of the person to whom the task "
                            "is assigned\nor 'd' if you want to change the"
                            " due date of the task\nor any other button to choose another task: ")
        edit_task_choice = validate_username(display_choices)

        if edit_task_choice == 'n':
            change_username(username_password, user_task_choice, task_list)

        if edit_task_choice == 'd':
            task_list[int(user_task_choice) - 1]['due_date'] = date_validation()
            write_tasks_to_file(task_list, path_tasks_txt)
    else:
        print("This task is already completed.")
##===========================================================================