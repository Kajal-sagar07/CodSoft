def add_task(tasks, task):
    tasks.append(task)
    print(f'Task "{task}" added.')

def remove_task(tasks, task):
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" removed."')
    else:
        print(f'Task "{task}" not found.')

def view_tasks(tasks):
    if tasks:
        print("Your To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f'{idx}. {task}')
    else:
        print("Your To-Do List is empty.")

def main():
    tasks = []
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(tasks, task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(tasks, task)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
