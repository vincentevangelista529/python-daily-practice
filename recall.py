import json

def load_tasks():
    try:
        with open ("task.json", "r") as file:
         return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    with open("task.json", "w") as file:
        json.dump(tasks, file, indent=4)

def get_non_empty_input(prompt):
    value = input(prompt).strip()
    while not value:
        print("Cannot be empty.")
        value = input(prompt).strip()
    return value

def add_task(tasks):
    work = {}
    work ["todo"] = get_non_empty_input("Enter Task Title: ")
    work ["done"] = False
    tasks.append(work)
    save_tasks(tasks)
    print("Task Saved Successfully!")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return

    print("\n--- Tasks ---")
    for index, task in enumerate(tasks, start=1):
        status = "✔" if task.get("done") else " "
        print(f"{index}. [{status}] {task['todo']}")

def mark_task_done(tasks):
    if not tasks:
        print("No tasks to mark.")
        return

    show_tasks(tasks)

    choice = input("Enter task number to mark as done: ")

    if not choice.isdigit():
        print("Enter a valid number.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(tasks):
        print("Task number out of range.")
        return

    tasks[index]["done"] = True
    save_tasks(tasks)
    print("Task marked as done!")

def delete_task(tasks):
    if not tasks:
        print("No Task To Delete. ")
        return
    
    show_tasks(tasks)

    choice = input("Enter a number to delete: ")

    if not choice.isdigit():
        print("Enter a number!")
        return
    
    index = int(choice) -1 

    if index <0 or index >= len(tasks):
        print("Task Number out of range")
        return
    
    deleted_task = tasks.pop(index)
    save_tasks(tasks)

    print(f"Deleted task: {deleted_task['todo']}")



tasks = load_tasks()

while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        show_tasks(tasks)
    elif choice == "3":
        mark_task_done(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
