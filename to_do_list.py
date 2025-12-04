tasks = []

while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Quit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        print("\nYour tasks:")
        for t in tasks:
            print("-", t)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")
