import time, sys

#defines the typingPrint function
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

#Empty list to store tasks
tasks = []

#Define function to add a task to the list
def add_task(task):
    tasks.append(task)
    typingPrint(f"Task '{task}' added successfully.")

#Define function to remove a task from the list
def delete_task(task):
    tasks.remove(task)
    typingPrint(f"Task '{task}' removed successfully.")

#Define function to view tasks in list
def view_tasks():
    if tasks:
        print("Tasks:")
        for task in tasks:
            typingPrint(f"- {task}")
    else:
        typingPrint("No tasks in list.")

#Main programme loop
while True:
    print("\nOptions:")
    typingPrint("1. Add Task")
    typingPrint("2. Delete Task")
    typingPrint("3. View Tasks")
    typingPrint("4. Quit")
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
        typingPrint("Invalid choice, please select 1-4")
