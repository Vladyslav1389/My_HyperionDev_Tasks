import os
import All_done_functions
from datetime import datetime, date

# DATETIME_STRING_FORMAT = "%Y-%m-%d"

# username_password ={'admin': "admin"}
# task_list = [{'task_ID': 1, 'username': 'admin', 'title': 'Add functionality to task manager',
#                'description': 'Add additional options and refactor the code.', 'due_date': "2022-12-01",
#                  'assigned_date': "2022-12-01", 'completed': False}]

# '''Allow a user to add a new task to task.txt file
#             Prompt a user for the following: 
#              - A username of the person whom the task is assigned to,
#              - A title of a task,
#              - A description of the task and 
#              - the due date of the task.'''
# new_task_ID = input("Task id: ")
# task_username = All_done_functions.validate_username("Name of person assigned to task: ")
# if task_username not in username_password.keys():
#     print("User does not exist. Please enter a valid username")
#     # continue
# task_title = input("Title of Task: ")
# task_description = input("Description of Task: ")
# while True:
#     try:
#         task_due_date = input("Due date of task (YYYY-MM-DD): ")
#         due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
#         break

#     except ValueError:
#         print("Invalid datetime format. Please use the format specified")


# # Then get the current date.
# curr_date = date.today()
# ''' Add the data to the file task.txt and
#     Include 'No' to indicate if the task is complete.'''
# new_task = {
#     "task_ID": new_task_ID,
#     "username": task_username,
#     "title": task_title,
#     "description": task_description,
#     "due_date": due_date_time,
#     "assigned_date": curr_date,
#     "completed": False
# }

# # task_list.append(new_task)
# # with open("tasks.txt", "w") as task_file:
# #     task_list_to_write = []
# #     for t in task_list:
# #         str_attrs = [
# #             t['task_ID'],
# #             t['username'],
# #             t['title'],
# #             t['description'],
# #             t['due_date'].strftime(DATETIME_STRING_FORMAT),
# #             t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
# #             "Yes" if t['completed'] else "No"
# #         ]
# #         task_list_to_write.append(";".join(str_attrs))
# #     task_file.write("\n".join(task_list_to_write))
# # print("Task successfully added.")
# # print(task_list)

DATETIME_STRING_FORMAT = "%Y-%m-%d"

with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")
    print(user_data)
    print(type(user_data))

username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password
print(username_password)

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
# print(f"task_list={task_list}")

##=-================================================================L
# def list_of_all_users(task_list_parameter):
#     for task in task_list_parameter:
#         print(task['username'])
#         # for user in task:
#         all_users = []
#         all_users.append(task['username'])
#     return all_users
# print('-'*80)
# print(list_of_all_users(user_data))
##=-================================================================L

def list_of_all_users(task_list_parameter):
    for task in task_list_parameter:
        print(type(task))
        print(task)
        # for user in task:

        # all_users = task.keys()
        all_users = task.keys()
    return all_users

print('-'*80)
print(list_of_all_users(username_password))