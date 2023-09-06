import time, sys

# Defines the typingPrint function
def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

# Empty list to store tasks
tasks = []

# Define function to add a task to the list
def add_task(task):
    tasks.append(task)
    typingPrint(f"Task '{task}' added successfully.")

# Define function to remove a task from the list
def delete_task(task_number):
    if 1 <= task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        typingPrint(f"Task '{deleted_task}' removed successfully.")
    else:
        typingPrint("Invalid task number. Please select a valid task to delete.")

# Define function to view tasks in list
def view_tasks():
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            typingPrint(f"{index}. {task}\n")
    else:
        typingPrint("No tasks in list.")

# Main program loop
while True:
    print("\nOptions:")
    typingPrint("1. Add Task\n")
    typingPrint("2. Delete Task\n")
    typingPrint("3. View Tasks\n")
    typingPrint("4. Quit\n")
    # Create choice variable input
    choice = input("Enter your choice >")

    if choice == '1':
        task = input("Enter task >")
        add_task(task)
    elif choice == '2':
        view_tasks()
        task_number = int(input("Enter the number of the task to delete >"))
        delete_task(task_number)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        break
    else:
        typingPrint("Invalid choice, please select 1-4")
