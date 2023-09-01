from datetime import datetime
import os

task_list = {}


def display_menu():
    print("1. Add a task\t 2. Show tasks\t 3. Mark as completed\t 4. Quit")


def add_task():
    task = input("Add a task: ")
    time = datetime.now()
    index = int(len(task_list) + 1)
    task_list[index] = {"task": task, "time": time, "completed": "Not completed"}
    print("Task added!")


def display_tasks():
    for i in range(1, len(task_list) + 1):
        print(f"{i}.")
        for values in task_list[i].values():
            print(values)


def mark_done():
    done_task = int(input("Which task do you want to mark as completed?"))
    task_list[done_task]['completed'] = "Completed"


def save_to_file():
    path = "C:/Users/marce/Desktop/codes/to-do-list"

    if os.path.exists(path):
        file = open("to-do-list.txt", "a")
        for i in range(1, len(task_list) + 1):
            file.write(f"{i}. {task_list[i].values()}")
        file.close()


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
        save_to_file()
        break
