#Empty list to store tasks
tasks = []

#Define function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added successfully.")

#Define function to remove a task from the list
def delete_task(task):
    tasks.remove(task)
    print(f"Task '{task}' removed successfully.")

#Define function to view tasks in list
def view_tasks():
    if tasks:
        print("Tasks:")
        for task in tasks:
            print(f"- {task}")
    else:
        print("No tasks in list.")

#Main programme loop
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Quit")
#Create choice variable input
    choice = input("Enter your choice >")

    if choice == '1':
        task = input("Enter task >")
        add_task(task)
    elif choice == '2':
        task = input("Delete task >")
        delete_task(task)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid choice, please select 1-4")
