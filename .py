#Author: James Grayer
#Program: Mod_6 - Mini Portfolio 1
#Date: Sept, 28, 2026

import json

def load_tasks(filename="tasks.json"):
    """Loads tasks from a JSON file. Handles missing file errors."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return empty list if file doesn't exist yet

def save_tasks(tasks, filename="tasks.json"):
    """Saves the current task list to a JSON file."""
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def show_menu():
    """Displays the user interface menu."""
    print("\n--- TASK MANAGER ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks(tasks):
    """Prints all tasks with their index number."""
    if not tasks:
        print("\nNo tasks found!")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def add_task(tasks):
    """Adds a new task to the list."""
    new_task = input("\nEnter the task description: ").strip()
    if new_task:
        tasks.append(new_task)
        print(f"Success: '{new_task}' added.")
    else:
        print("Error: Task description cannot be empty.")

def delete_task(tasks):
    """Deletes a task by its list index, including input validation."""
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        choice = int(input("\nEnter the number of the task to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"Success: '{removed}' deleted.")
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")

def main():
    """Main program execution loop."""
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

PS G:\Users\James\AppData\Local\Programs\Microsoft VS Code> & C:\Users\James\AppData\Local\Python\pythoncore-3.14-64\python.exe c:/Users/James/.vscode/.py

--- TASK MANAGER ---
1. View Tasks
2. Add Task
3. Delete Task
4. Exit

Choose an option (1-4): 1

Your Tasks:
1. load tasks from JSON file
2. main program execution loop

--- TASK MANAGER ---
1. View Tasks
2. Add Task
3. Delete Task
4. Exit

Choose an option (1-4): 3

Your Tasks:
1. load tasks from JSON file
2. main program execution loop

Enter the number of the task to delete: 2
Success: 'main program execution loop' deleted.

--- TASK MANAGER ---
1. View Tasks
2. Add Task
3. Delete Task
4. Exit

Choose an option (1-4): 4

Goodbye!
PS G:\Users\James\AppData\Local\Programs\Microsoft VS Code> 
