class TaskManager:
    def __init__(self):
        self.tasks = []
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                cleaned_task = line.strip()
                if cleaned_task:
                    self.tasks.append(cleaned_task)
    
    def view_tasks(self):
        if not self.tasks:
            print("There are no tasks!")
        else:
            print("Your tasks:")
            for num, task in enumerate(self.tasks, 1):
                print(f"{num}. {task}")

    def add_task(self):
        new_task = input("What task do you want to add?: ")
        self.tasks.append(new_task)
        print("The task was added!")

        with open("tasks.txt", "w") as my_file:
            for task in self.tasks:
                my_file.write(task + "\n")

    def remove_task(self):
        if not self.tasks:
            print("There are no tasks to remove!")
            return
        
        self.view_tasks()
        try:
            task_remove_num = int(input("What task do you want to remove (write its number): "))
            if index < 0 or index >= len(self.tasks):
                print("Invalid task number! Please choose from the list.")
                return
            
            index = task_remove_num -1
            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task}' was removed!")

            print("Your task was removed!")

            with open("tasks.txt", "w") as my_file:
                for task in self.tasks:
                    my_file.write(task + "\n")
    
        except ValueError:
                print("Please enter a valid number!")

print("Welcome to your Task Manager!")

manager = TaskManager()
while True:
    action = input("What would you like to do?\n" \
    "1. View tasks\n" \
    "2. Add task\n" \
    "3. Remove task\n" \
    "4. Exit\n" \
    "Your choice: ")

    if action in ["1", "view", "see"]:
        manager.view_tasks()
    elif action in ["2", "add", "new"]:
        manager.add_task()
    elif action in ["3", "remove", "delete", "del"]:
        manager.remove_task()
    elif action in ["4", "exit", "quit", "q"]:
        print("Goodbye! See you soon!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, 3 or 4.")
