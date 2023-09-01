from datetime import datetime
import os

task_list = {}


def display_menu():
    print("1. Add a task\t 2. Show tasks\t 3. Mark as completed\t 4. Quit")


# def load_tasks_from_file():
#     file = "to-do-list.txt"
#     if os.path.exists(file):
#         with open(file, "r") as file:
#             for line in file:
#                 parts = line.strip().split('.')
#                 if len(parts) == 4:
#                     index, rest = parts
#                     task, time, completed = rest.split(', ')
#                     task_list[int(index)] = {"task": task, "time": time, "completed": completed}


def save_to_file():
    file = "to-do-list.txt"
    with open(file, "w") as file:
        for index, task_info in task_list.items():
            task_str = f"{index}. {task_info['task']}, {task_info['time']}, {task_info['completed']}\n"
            file.write(task_str)


def add_task():
    task = input("Add a task: ")
    time = str(datetime.now())
    index = len(task_list)
    task_list[index] = {"task": task, "time": time, "completed": "Not completed"}
    save_to_file()
    print("Task added!")


def display_tasks():
    for index, task_info in task_list.items():
        print(f"{index}. Task: {task_info['task']}, Time: {task_info['time']}, Status: {task_info['completed']}")


def mark_done():
    done_task = int(input("Which task do you want to mark as completed?"))
    if done_task in task_list:
        task_list[done_task]['completed'] = "Completed"
        save_to_file()
        print("Marked as completed!")
    else:
        print("Task not found!")


# load_tasks_from_file()

while True:
    display_menu()
    user_input = int(input("What do you want to do? "))

    if user_input == 1:
        add_task()
    elif user_input == 2:
        display_tasks()
    elif user_input == 3:
        mark_done()
    elif user_input == 4:
        break
