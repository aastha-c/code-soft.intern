import sys

def show_menu():
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")

def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: "))
    if 0 < task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        print(f"Task '{removed}' deleted.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
