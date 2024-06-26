""" Task 1: A To-Do List application is a useful project that helps users manage and organize 
their tasks efficiently. This project aims to create a command-line or GUI-based application 
using Python, allowing users to create, update, and track their to-do lists"""

import json
import os

f = 'todo_list.json'


def load_tasks():
    if not os.path.isfile(f):
        return []
    with open(f, 'r') as file:
        return json.load(file)


def save_tasks(tasks):
    with open(f, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(task):
    tasks = load_tasks()
    tasks.append({'task': task, 'completed': False})
    save_tasks(tasks)
    print(f"Added task: {task}")


def update_task(index, new_task):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]['task'] = new_task
        save_tasks(tasks)
        print(f"Updated task #{index + 1} -> {new_task}")
    else:
        print("Invalid task number.")


def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted task #{index + 1}: {removed_task['task']}")
    else:
        print("Invalid task number.")


def show_tasks():
    tasks = load_tasks()
    i = 0
    if not tasks:
        print("No tasks found.")
    for task in tasks:
        if task['completed']:
            print(f"{i+1}. {task['task']} --> [Completed]")
        else:
            print(f"{i+1}. {task['task']} --> [Pending]")
        i += 1


def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        save_tasks(tasks)
        print(f"Completed task #{index + 1}: {tasks[index]['task']}")
    else:
        print("Invalid task number.")


def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add a Task")
        print("2. Update a Task")
        print("3. Delete a Task")
        print("4. Show all Tasks")
        print("5. Complete a Task")
        print("6. Exit\n")

        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            show_tasks()
            index = int(input("\nEnter task number to update: "))
            new_task = input("Enter the new task: ")
            update_task(index-1, new_task)
        elif choice == '3':
            show_tasks()
            index = int(input("\nEnter task number to delete: "))
            delete_task(index-1)
        elif choice == '4':
            show_tasks()
        elif choice == '5':
            show_tasks()
            index = int(input("\nEnter task number to complete it: "))
            complete_task(index-1)
        elif choice == '6':
            print("Thank You!\n")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()
