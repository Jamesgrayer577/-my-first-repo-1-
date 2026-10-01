#Author: James Grayer
#Program: Mod_6 - Mini Portfolio 1
#Date: October 1, 2026

# task_manager.py
# Mini Portfolio I: Task Management System
# Purpose: A command-line tool to add, view, complete, and delete daily tasks.

import sys

# Global data structure: A list of dictionaries to store tasks.
# Each task dictionary will have keys: 'id', 'title', and 'status'.
todo_list = []
task_id_counter = 1


def display_menu():
    """Prints the main application menu to the console."""
    print("\n" + "=" * 30)
    print("      DAILY TASK MANAGER      ")
    print("=" * 30)
    print("1. View Current Tasks")
    print("2. Add a New Task")
    print("3. Mark Task as Complete")
    print("4. Delete a Task")
    print("5. Exit Application")
    print("=" * 30)


def view_tasks():
    """Displays all tasks currently in the todo_list."""
    if not todo_list:
        print("\n[!] Your task list is currently empty.")
        return

    print("\n--- YOUR TASKS ---")
    print(f"{'ID':<5}{'Task Title':<35}{'Status'}")
    print("-" * 50)
    for task in todo_list:
        # Use a ternary operator to print a visual checkbox status
        status_icon = "[✔] Complete" if task["status"] else "[ ] Pending"
        print(f"{task['id']:<5}{task['title']:<35}{status_icon}")


def add_task():
    """Prompts user for a task title, validates it, and appends it to the list."""
    global task_id_counter
    print("\n--- ADD NEW TASK ---")
    title = input("Enter the task description: ").strip()

    # Bug Prevention: Validate against empty strings
    if not title:
        print("[Error] Task description cannot be empty.")
        return

    # Construct the dictionary and append to our main list
    new_task = {"id": task_id_counter, "title": title, "status": False}
    todo_list.append(new_task)
    print(f"[Success] Task #{task_id_counter} added: '{title}'")

    # Increment counter so the next task gets a unique identifier
    task_id_counter += 1


def mark_complete():
    """Finds a task by ID and sets its completion status to True."""
    print("\n--- MARK TASK AS COMPLETE ---")
    view_tasks()

    if not todo_list:
        return

    try:
        # Exception Handling: Guard against non-integer strings
        target_id = int(input("\nEnter the ID of the task to complete: "))
    except ValueError:
        print("[Error] Invalid input. Please enter a valid numerical ID.")
        return

    # Loop through the list to find the matching task dictionary
    for task in todo_list:
        if task["id"] == target_id:
            if task["status"]:
                print("[!] This task is already marked complete.")
            else:
                task["status"] = True
                print(f"[Success] Task #{target_id} is now complete!")
            return

    # Executed only if the loop finishes without hitting the 'return' statement
    print(f"[Error] Task ID {target_id} not found.")


def delete_task():
    """Removes a task from the list using its unique ID."""
    print("\n--- DELETE A TASK ---")
    view_tasks()

    if not todo_list:
        return

    try:
        target_id = int(input("\nEnter the ID of the task to delete: "))
    except ValueError:
        print("[Error] Invalid input. Please enter a valid numerical ID.")
        return

    # Search and destroy approach using list enumeration
    for index, task in enumerate(todo_list):
        if task["id"] == target_id:
            removed_task = todo_list.pop(index)
            print(f"[Success] Deleted task: '{removed_task['title']}'")
            return

    print(f"[Error] Task ID {target_id} not found.")


def main():
    """Main execution loop driving the menu choices."""
    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("\nThank you for using Daily Task Manager. Goodbye!")
            sys.exit()  # Cleanly terminates the program execution
        else:
            print("[Error] Invalid choice. Please pick a number from 1 to 5.")


# Standard Python boilerplate to ensure script runs only when executed directly
if __name__ == "__main__":
    main()

ADD NEW TASK ---
Enter the task description: Task ID
[Success] Task #1 added: 'Task ID'

==============================
      DAILY TASK MANAGER
==============================
1. View Current Tasks
2. Add a New Task
3. Mark Task as Complete
4. Delete a Task
5. Exit Application
==============================
Select an option (1-5): 2

--- MARK TASK AS COMPLETE ---

--- YOUR TASKS ---
ID   Task Title                         Status
--------------------------------------------------
1    Task ID                            [ ] Pending
2    {"id": task_id_counter, "title": title, "status": False}[ ] Pending
3    .strip()                           [ ] Pending

    
