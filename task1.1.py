#Mini-Project: To-Do List Application
#  Welcome to the To-Do List APP

to_do_list=[]
complete_task=[]
def list_app():

    while True:
        try:
            print("Welcome to the To-Do List App!")
            print("")
            print("Menu:")
            print("1. Add a task")
            print("2. Mark a task as complete")
            print("3. View tasks")
            print("4. Delete a task")
            print("5. Quit")
#Ask for what task they want to do
        
            choice = (input("What would you like to do, please enter a number: "))
#ask for there new task
            if choice == "1":
                add_task =input("What is the new task you would like to do: ").lower()
                print(f"{add_task} has been added to your To-Do-List")
                to_do_list.append(add_task)
#ask for completed task
            elif choice == "2":
                completed_task =input("What task would you like to mark as complete: ").lower()
                print(f"{completed_task} has been marked as complete")
                complete_task.append(completed_task)
                to_do_list.remove(completed_task)
# Views both the completed list and incompleted list
            elif choice =="3":
                print (f"Your incomplete task are :{to_do_list} ")
                print(f"Your completed task are {complete_task}")
#deletes a task
            elif choice =="4":
                delete_task =input("What task would you like to delete? ").lower()
                print(f"{delete_task} has been removed from your To-Do-List")
                to_do_list.remove(delete_task)
                complete_task.remove(delete_task)
#end the to do list app
            elif choice =="5":
                print("Thank You, Goodbye")
                break
#handles any errors 
            else: print("Please enter a value from 1-5")
        except ValueError:
            print("Sorry invald entry please enter a number from 1-5")
list_app()
   
            