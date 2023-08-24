import time

class Task:
    def __init__(self, title, due_date, priority, status = "To Do"):
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.status = status

class Task_Manager:
    def __init__(self):
        self.task = []

    def add_task(self, title, due_date, Priority):
        task = Task(title, due_date, Priority)
        self.task.append(task)
    
    def update_task(self, title, new_status):
        for task in self.task:
            if task.title == title:
                task.status = new_status
                break

    def list_tasks(self):
        for task in self.task:
                print(f"Title: {task.title}")
                print(f"Due Date: {task.due_date}")
                print(f"Priority: {task.priority}")
                print(f"Status: {task.status}")
                print("-" * 30)
          
def App():
    task_manager_app = Task_Manager()

    while True:
        print("Welcome to your Task Management Console App, what would you like to do: ")
        time.sleep(1)
        print("1. Add Task")
        time.sleep(1)
        print("2. Update Task Status")
        time.sleep(1)
        print("3. List Tasks")
        time.sleep(1)
        print("4. Quit")
        print('\n')

        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter task title: ")
            due_date = input("Enter task due date: ")
            priority = input("What is the Priority level of this task: ")
            task_manager_app.add_task(title, due_date, priority)
            print("Task added successfully.")
            print('\n')

        elif choice == 2:
            title = input("Enter task title: ")
            new_status = input("Enter new status (In Progress, QA, Postponed, Done): ")
            task_manager_app.update_task(title, new_status)
            print("Task status updated successfully.")
            print('\n')
            

        elif choice == 3:
            task_manager_app.list_tasks()
            print('\n')

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

App()