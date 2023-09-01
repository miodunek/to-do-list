from datetime import datetime
import os

task_list = {}


def display_menu():
    print("1. Add a task\t 2. Show tasks\t 3. Mark as completed\t 4. Quit")


def save_to_file(task_index):
    path = "C:/Users/marce/Desktop/codes/to-do-list"

    if os.path.exists(path):
        file = open("to-do-list.txt", "a")

        file.write(f"{task_index}.")
        for values in task_list[task_index].values():
            file.write(values + " ")
        file.write("\n")
        file.close()
    else:
        print("File not found")


def add_task():
    task = input("Add a task: ")
    time = str(datetime.now())
    index = int(len(task_list) + 1)
    task_list[index] = {"task": task, "time": time, "completed": "Not completed"}
    save_to_file(index)
    print("Task added!")


def display_tasks():
    file = open("to-do-list.txt", "r")
    data = file.read()
    print(data)
    file.close()


def mark_done():
    done_task = int(input("Which task do you want to mark as completed?"))
    task_list[done_task]['completed'] = "Completed"
    file = open("to-do-list.txt", "r")
    data = file.read()
    data = data.replace(task_list[done_task]['completed'], 'Completed')
    file.close()
    file = open("to-do-list.txt", "w")
    file.write(data)
    file.close()
    print("Marked as completed!")


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
