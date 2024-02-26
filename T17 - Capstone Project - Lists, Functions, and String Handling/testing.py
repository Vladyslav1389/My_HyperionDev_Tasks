import os
import All_done_functions
from datetime import datetime, date

def clear_screen():
    """Clear the console screen"""
    os.system("cls||clear")
    
def line_print():
    print(symbol='=', length=79)



# # def file_exist_check(path_parametr):
# #     if not os.path.exists(path_parametr):
# #     with open(path_parametr, "w") as default_file:
# #         pass


# if not os.path.exists("user.txt"):
#     with open("user.txt", "w") as default_file:
#         default_file.write("admin;password")

# # Read in user_data
# with open("user.txt", 'r') as user_file:
#     user_data = user_file.read().split("\n")

# # Convert to a dictionary
# username_password = {}
# for user in user_data:
#     username, password = user.split(';')
#     username_password[username] = password
# print(username_password)

username_password = {'admin': "password"}
All_done_functions.reg_user(username_password)

# print(username_password)

clear_screen()

# import os
# from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    print(task_data)
    task_data = [t for t in task_data if t != ""]
    print(task_data)


task_list = []
for task_ID, t_str in enumerate(task_data, 1):
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t["task_ID"] = task_ID
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)
  # The `print(task_list)` statement is printing the contents of the `task_list`
  # variable. This variable is a list of dictionaries, where each dictionary
  # represents a task with various attributes such as Task ID, username, title,
  # description, due date, assigned date, and completion status.
    print(task_list)


for t in task_list:
    disp_str = f"Task: \t\t {t['title']}\n"
    disp_str += f"Assigned to: \t {t['username']}\n"
    disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    disp_str += f"Task Description: \n {t['description']}\n"
    print(disp_str)

##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# elif menu == 'a':
'''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
new_task_ID = input("Task id: ")
task_username = All_done_functions.validate_username("Name of person assigned to task: ")
if task_username not in username_password.keys():
    print("User does not exist. Please enter a valid username")
    # continue
task_title = input("Title of Task: ")
task_description = input("Description of Task: ")
while True:
    try:
        task_due_date = input("Due date of task (YYYY-MM-DD): ")
        due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
        break

    except ValueError:
        print("Invalid datetime format. Please use the format specified")


# Then get the current date.
curr_date = date.today()
''' Add the data to the file task.txt and
    Include 'No' to indicate if the task is complete.'''
new_task = {
    "task_ID": new_task_ID,
    "username": task_username,
    "title": task_title,
    "description": task_description,
    "due_date": due_date_time,
    "assigned_date": curr_date,
    "completed": False
}

task_list.append(new_task)
with open("tasks.txt", "w") as task_file:
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
print("Task successfully added.")
print(task_list)




# clear_screen()
# curr_user = "admin"
# ''' Reads the task from task.txt file and prints to the console in the 
#            format of Output 2 presented in the task pdf (i.e. includes spacing
#            and labelling)
#         '''
# for t in task_list:
#     if t['username'] == curr_user:
#         disp_str = f"Task: \t\t {t['title']}\n"
#         disp_str += f"Assigned to: \t {t['username']}\n"
#         disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
#         disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
#         disp_str += f"Task Description: \n {t['description']}\n"
#         print(disp_str)