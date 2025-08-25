#create a empty list to store tasks
todo_list=[]
#main function
def main():
    try:
        #function for add task
        def add_task():
            task=input("enter the task:")
            todo_list.append({"task":task,"status":"task pending"})
            print("task added susscefully\n")          
        #function for view task
        def view_task():
            if len(todo_list)==0:
                print("there is no task")
            else:
                for index,task in enumerate(todo_list,1):
                    print(f"{index}:{task['task']} - {task['status']}")
            print("\n")
                
        #function for mark task
        def mark_task_completed():
            if len(todo_list)==0:
                print("no tasks")
            else:
                index=int(input("enter the task you want to mark:")) -1
                if 0 <=index <len(todo_list):
                    todo_list[index]['status']="marked"
                    print(f"task {todo_list[index]["task"]} has been marked")        
                else:
                    print("invalid task nuber\n")
        def exit():
            print("visit again\n")
            
        #display menu    
        while(True):
            print("1.add a task")
            print("2.view all tasks")
            print("3.mark a task comleted")
            print("4.exit")
            print("\n")
            
            choice=int(input("enter a choice:"))
            if choice==1:
                add_task()
            elif choice==2:
                view_task()
            elif choice==3:
                mark_task_completed()
            elif choice==4:
                exit()
            else:
                print("invallid number")
    except Exception as e:
        print(e)
        
main()

