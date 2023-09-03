from datetime import datetime
import os

task_list = {}
next_index = 1


def display_menu():
    print("1. Add a task\t 2. Show tasks\t 3. Mark as completed\t 4. Quit")


def load_tasks_from_file():
    global next_index
    file = "to-do-list.txt"
    if os.path.exists(file):
        with open(file, "r") as file:
            for line in file:
                parts = line.strip().split('. ')
                if len(parts) == 2:
                    index, rest = parts
                    task, time, completed = rest.split(', ')
                    index = int(index)
                    task_list[index] = {"index": index, "task": task, "time": time, "completed": completed}
                    next_index = max(next_index, index + 1)


def save_to_file():
    file = "to-do-list.txt"
    with open(file, "a") as file:
        for index, task_info in task_list.items():
            if 'index' not in task_info:
                task_info['index'] = index
            task_str = f"{task_info['index']}. {task_info['task']}, {task_info['time']}, {task_info['completed']}\n"
            file.write(task_str)


def add_task():
    global next_index
    task = input("Add a task: ")
    time = str(datetime.now())
    index = next_index
    task_list[index] = {"task": task, "time": time, "completed": "Not completed"}
    next_index += 1
    save_to_file()
    print("Task added!")


def display_tasks():
    for task_info in sorted(
            task_list.values(),
            key=lambda x: x['index']
    ):
        print(
            f"{task_info['index']}. Task: {task_info['task']}, "
            f"Time: {task_info['time']}, "
            f"Status: {task_info['completed']}"
        )


def mark_done():
    done_task = int(input("Which task do you want to mark as completed?"))
    if done_task in task_list:
        task_list[done_task]['completed'] = "Completed"
        save_to_file()
        print("Marked as completed!")
    else:
        print("Task not found!")


load_tasks_from_file()

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
