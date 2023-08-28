def view_tasks():
    print("Your Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{index}. [{status}] {task['task']}")

tasks = []

while True:
    print("To-Do List:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Add the task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added!")

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        view_tasks()
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print("Task marked as completed!")

    elif choice == "4":
        view_tasks()
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            del tasks[task_num - 1]
            print("Task deleted!")

    elif choice == "5":
        print("Have A Nice Day!")
        break

    else:
        print("Please choose a valid option.")
print("Happy Coding")
