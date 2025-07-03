tasks = []
numb = 1

while True:
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
        tasks = [t for t in tasks if not t.startswith(f"{del_num}:")]
    
    elif task == "q":
        print("Goodbye")
        break
    
    else:
        print("Invalid input")




'''
task = "b"
tasks = ""
numb = 1

while task != "q":
    task = input("What would you like to do: \n a. Add \n d. Delete \n v. View \n q. Quit \n > ")
    if task == "a":
        tasks = tasks + "\n " + str(numb) + ": " + input("Enter a task: ")
        numb = numb + 1
    elif task == "v":
        print(tasks)
    elif task == "q":
        print("Goodbye")
    elif task == "d":
        tasks = tasks.replace(input("Enter the task number to delete: ") + ": ", "")
        numb = numb - 1
    else:
        print("Invalid input")
'''