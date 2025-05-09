# todo.py

tasks = []

def add_task(task):
    tasks.append({'task': task, 'completed': False})
    print(f"✅ Task '{task}' added!")

def show_tasks():
    if not tasks:
        print("📭 No tasks found.")
    else:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task['completed'] else "❌"
            print(f"{i}. {status} {task['task']}")

def delete_task(index):
    try:
        removed = tasks.pop(index - 1)
        print(f"🗑️ Task '{removed['task']}' deleted.")
    except IndexError:
        print("⚠️ Invalid task number.")

def complete_task(index):
    try:
        tasks[index - 1]['completed'] = True
        print(f"🎉 Task '{tasks[index - 1]['task']}' marked as completed!")
    except IndexError:
        print("⚠️ Invalid task number.")

def edit_task(index, new_task):
    try:
        old_task = tasks[index - 1]['task']
        tasks[index - 1]['task'] = new_task
        print(f"✏️ Task '{old_task}' updated to '{new_task}'.")
    except IndexError:
        print("⚠️ Invalid task number.")
def main():
    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Edit Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            show_tasks()
            try:
                index = int(input("Enter the task number to delete: "))
                delete_task(index)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == '4':
            show_tasks()
            try:
                index = int(input("Enter the task number to mark as completed: "))
                complete_task(index)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == '5':  # New option to edit tasks
            show_tasks()
            try:
                index = int(input("Enter the task number to edit: "))
                new_task = input("Enter the new task description: ")
                edit_task(index, new_task)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == '6':
            print("👋 Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 6.")
if __name__ == "__main__":
    main()
