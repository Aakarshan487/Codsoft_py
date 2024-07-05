print("!!!WELCOME TO TO-DO LIST!!!")
task = []

close = "c"

while close == "c": 
    print("a - add")
    print("e - edit")
    print("f - finished")
    print("d - delete")
    do = input("Add/Edit/Delete/Finished:").lower()

    try:
        if do == "a":
            print("ADD TASK:")
            taskadd = input("Enter your task here:")
            task.append(taskadd)
        
        elif do == "e":
            print("EDIT TASK:")
            taskedit = int(input("Enter task number to 'edit' (eg,1/2/3..):"))
            task[taskedit-1] = input("Enter the new task here:")
        
        elif do == "d":
            print("DELETE TASK:")
            taskdel = int(input("Enter task number to 'delete' (eg,1/2/3..):"))
            task.pop(taskdel-1)
        
        elif do == "f":
            print("FINISHED TASK:")
            taskdone = int(input("Enter task number finished (eg,1/2/3..):"))
            print(task[taskdone-1],"(DONE)")
            task[taskdone-1] = task[taskdone-1],"(Done)"
        
    except Exception as e:
        print("Invalid Input:",e)

    sno=1
    for lists in task:
        print(f"{sno}.) {lists}")
        sno = sno+1

    close = input("Press any letter to exit/press 'c' to continue:").lower()

print()
