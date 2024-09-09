tasks=[]

def addtask():
    task=input("please enter the task : ")
    tasks.append(task)
    print(f"Task '{task}'added to the list")

def listtask():
    if not tasks:
        print("there are no tasks currently")
    else:
        print("current task")
        for i,task in enumerate(tasks):
            print("task",i,task)

def deletetask():
    listtask()
    try:
        taskTodelete=int(input("Enter the task to delete"))
        if taskTodelete  >=0 and taskTodelete < len(tasks):
              tasks.pop(taskTodelete)
              print(f"task {taskTodelete} to delete has removed")
        else:
              print(f"task {taskTodelete} to delete is not found")

    except:
        print("Invalid input.")    
    

if __name__=="__main__":
    print("welcome to the to do list app:")
    while True:
        print("\n")
        print("please select one of the following options")
        print("_________________________")
        print("1. add a new task")
        print("2. delete a task")
        print("3. list tasks")
        print("4. quit")
        choice = input("Enter your choice : ")

        if(choice =="1"):
            addtask()

        elif(choice =="2"):
            deletetask()

        elif(choice =="3"):
            listtask()

        elif(choice =="4"):
            break

        else:
            print("Invalid input,please try again")

    print("Good Bye !")
