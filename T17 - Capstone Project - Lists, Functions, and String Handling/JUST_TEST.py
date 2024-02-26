import os
import All_done_functions
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

username_password ={'admin': "admin"}
task_list = [{'task_ID': 1, 'username': 'admin', 'title': 'Add functionality to task manager',
               'description': 'Add additional options and refactor the code.', 'due_date': "2022-12-01",
                 'assigned_date': "2022-12-01", 'completed': False}]

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