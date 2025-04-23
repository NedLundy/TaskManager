import datetime

tasks = []

def create_task():
    name = input("Task name: ")
    due = input("Due date (YYYY-MM-DD): ")
    priority = input("Priority (High/Medium/Low): ")
    desc = input("Description (optional): ")
    task = {
        "name": name,
        "due": due,
        "priority": priority,
        "desc": desc,
        "status": "to do",
        "completed_at": None
    }
    tasks.append(task)
    print("Task created!\n")

def list_tasks():
    for i, t in enumerate(tasks):
        print(f"{i+1}. {t['name']} [{t['status']}] - Due: {t['due']}, Priority: {t['priority']}")

def edit_task():
    list_tasks()
    idx = int(input("Enter task number to edit: ")) - 1
    if 0 <= idx < len(tasks):
        t = tasks[idx]
        t["name"] = input(f"New name (current: {t['name']}): ") or t["name"]
        t["due"] = input(f"New due date (current: {t['due']}): ") or t["due"]
        t["priority"] = input(f"New priority (current: {t['priority']}): ") or t["priority"]
        t["desc"] = input(f"New description (current: {t['desc']}): ") or t["desc"]
        print("Task updated!\n")
    else:
        print("Invalid task number.\n")

def delete_task():
    list_tasks()
    idx = int(input("Enter task number to delete: ")) - 1
    if 0 <= idx < len(tasks):
        del tasks[idx]
        print("Task deleted!\n")
    else:
        print("Invalid task number.\n")

def mark_completed():
    list_tasks()
    idx = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]["status"] = "completed"
        tasks[idx]["completed_at"] = str(datetime.datetime.now())
        print("Task marked as completed!\n")
    else:
        print("Invalid task number.\n")

def filter_tasks():
    term = input("Search by task name: ").lower()
    results = [t for t in tasks if term in t["name"].lower()]
    for i, t in enumerate(results):
        print(f"{i+1}. {t['name']} - Status: {t['status']}, Due: {t['due']}")

def update_status():
    list_tasks()
    idx = int(input("Enter task number to update status: ")) - 1
    if 0 <= idx < len(tasks):
        new_status = input("New status (to do/in progress/completed): ")
        if new_status in ["to do", "in progress", "completed"]:
            tasks[idx]["status"] = new_status
            print("Status updated!\n")
        else:
            print("Invalid status.\n")
    else:
        print("Invalid task number.\n")

#THIS IS FOR LE MENU
while True:
    print("\n--- Task Manager ---")
    print("1. Create task")
    print("2. Edit task")
    print("3. Delete task")
    print("4. Mark as completed")
    print("5. Search tasks")
    print("6. Update task status")
    print("7. Show all tasks")
    print("8. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        create_task()
    elif choice == '2':
        edit_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        mark_completed()
    elif choice == '5':
        filter_tasks()
    elif choice == '6':
        update_status()
    elif choice == '7':
        list_tasks()
    elif choice == '8':
        print("Bye!")
        break
    else:
        print("Invalid choice.\n")
