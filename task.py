tasks = []
numb = 1
new_tasks = []
end = "n"

while end != "q":
    task = input("What would you like to do: \n a. Add \n d. Delete \n v. View \n q. Quit \n > ")
    
    if task == "a":
        new_task = input("Enter a task: ")
        tasks.append(f"{numb}: {new_task}")
        numb += 1
    
    elif task == "v":
        if tasks:
            for t in tasks:
                print(t)
        else:
            print("No tasks yet!")
    
    elif task == "d":
        del_num = input("Enter the task number to delete: ")
        for task in tasks:
            if not task.startswith(del_num + ":"):
                new_tasks.append(task)
        tasks = new_tasks
    
    elif task == "q":
        print("Goodbye")
        end = "q"
    
    else:
        print("Invalid input")


