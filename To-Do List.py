print("Welcome to your To-Do List!") # This creates a title which says "Welcome to your To-Do List!"
tasks = []# This stores the task you add

while True:
    print("""
   1. Add task
   2. View task
   3. Quit
   """) # This is a menu which shows 3 options you want to choose from(Add task,View task,Quit)

    choice = input("Choice: ") # Enables you to choose an option

    if choice == "1": # This shows what happens when you use option 1
        while True: # This makes the code in choice 1 repeat multiple times / loop unless you type "quit"
            task = input("Enter a new task (or type 'quit' to stop): ") # This enables you to add a new task
            if task.lower() == "quit": 
                break # This code stops the loop when you type quit
            tasks.append(task)
            print("Task added!")


    elif choice == "2":# This displays the tasks you added when you enter option 2.
        print(" ")# This craetes a space
        print("Your tasks:")
        for i in range(len(tasks)):# This makes python know the number of tasks you added.
            print(f"{i+1}.{tasks[i]}")#This assigns the position(rank) of the task to the task.
#For example(if Washing was the first task.It would make it. "1. Washing")

    elif choice == "3":
        print("Goodbye!") # 
        break
        # It displays Goodbye when you choose option 3 and also stops the loop
    else:
        print("Invalid choice! Try again.")
    # This displays(invalid choice.!Try again) if you enter a choice whuch isn't 1 to 3



