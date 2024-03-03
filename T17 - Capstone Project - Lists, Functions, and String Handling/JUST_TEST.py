import os
import All_done_functions
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# def date_validation():
#     while True:
#         try:
#             task_due_date = input("Due date of task (YYYY-MM-DD): ")
#             due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
#             break

#         except ValueError:
#             print("Invalid datetime format. Please use the format specified")
#     curr_date = datetime.now()
#     if due_date_time.date() >= curr_date.date():
#         return due_date_time.date()
#     else:
#         print("The due date cannot be before the current date.")
#         return date_validation()

# print(date_validation())



##=====================================================================================
# # Then get the current date.
# curr_date = str(date.today())
# curr_date = datetime.strptime(curr_date, DATETIME_STRING_FORMAT)
# if curr_date < due_date_time:
#     print(curr_date,'<', due_date_time)
# else:
#     print("Not working")
##=====================================================================================


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

# DATETIME_STRING_FORMAT = "%Y-%m-%d"

# with open("user.txt", 'r') as user_file:
#     user_data = user_file.read().split("\n")
#     print(user_data)
#     print(type(user_data))

# username_password = {}
# for user in user_data:
#     username, password = user.split(';')
#     username_password[username] = password
# print(username_password)
# print(username_password.keys())


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
# # print(f"task_list={task_list}")

# ##=-================================================================L
# # def list_of_all_users(task_list_parameter):
# #     for task in task_list_parameter:
# #         print(task['username'])
# #         # for user in task:
# #         all_users = []
# #         all_users.append(task['username'])
# #     return all_users
# # print('-'*80)
# # print(list_of_all_users(user_data))
# ##=-================================================================L

# def list_of_all_users(task_list_parameter):
#     for task in task_list_parameter:
#         print(type(task))
#         print(task)
#         # for user in task:

#         # all_users = task.keys()
#         all_users = task.keys()
#     return all_users

# print('-'*80)
# print(list_of_all_users(username_password))
curr_date = datetime.now()

def uncompleted_overdue(task_list, curr_date):
    counter = 0
    for task in task_list:
        if task['completed'] == False and task['due_date'] <= curr_date:
            counter += 1
    return counter

print(uncompleted_overdue(task_list, curr_date))
