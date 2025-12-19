print("Welcome to your Task Manager!")

def view_tasks():
    with open("tasks.txt") as my_tasks:
        lines = my_tasks.readlines()
        for line in lines:
            print(line)
def add_task_to_list():
    with open("tasks.txt", "a") as my_tasks:
        new_task = input("What task do you want to add?: ")
        my_tasks.write(new_task + "\n")
        print("The task was added!")
# def del_task_from_list():
#     with open("tasks.txt", "a") as my_tasks:

def task_manager():
    while True:
        action_choice = input("What action whould you like to do:\n1. See my tasks \n2. Add task \n3. Remove task \n4. Exit \n")
        if action_choice in ["1", "see my tasks", 'see task']:
            view_tasks()
        elif action_choice in ['2', "add task", "new task"]:
            add_task_to_list()
        # elif action_choice in ['3', "del task", "delete"]:
        elif action_choice in ['4', 'exit', 'quit']:
            break


task_manager()
