print("Welcome to your To-Do List!")
tasks = []

while True:
    print("""
   1. Add task
   2. View task
   3. Quit
   """)

    choice = input("Choice: ")

    if choice == "1":
        while True:
            task = input("Enter a new task (or type 'quit' to stop): ")
            if task.lower() == "quit":
                break
            tasks.append(task)
            print("Task added!")


    elif choice == "2":
        print(" ")
        print("Your tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")



