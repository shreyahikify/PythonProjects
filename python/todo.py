tasks = []

def show_menu():
    print("\n1. Add Task | 2. View Tasks | 3. Remove Task | 4. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        new_task = input("Enter the task: ")
        tasks.append(new_task)
        print("Task added!")
    elif choice == '2':
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    elif choice == '3':
        task_num = int(input("Enter task number to remove: "))
        if 0 < task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid number.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")