todos = [] 
while True: 
    print("\n--- To-Do List ---") 
    print("1. Add task") 
    print("2. View tasks ") 
    print("3. Complete task") 
    print("4. Delete task") 
    print("5. Quit") 
    choice = input("\nEnter choice (1-5):") 
    if choice == "1": 
        task = input("Enter task:") 
        todos.append({"task": task, "done": False}) 
        print(f"Task added: {task}") 
    elif choice == "2": 
        if len(todos) == 0: 
            print("No task yet!") 
        else: 
            print("\nYour tasks:") 
            for i, todo in enumerate(todos): 
                status = "✅" if todo["done"] else"❌" 
                print(f"{i + 1}. [{status}] {todo['task']}") 
    elif choice == "3": 
        if len(todos) == 0: 
            print("No task yet!") 
        else: 
            for i, todo in enumerate(todos): 
                status = "✅" if todo["done"] else"❌" 
                print(f"{i + 1}. {todo['task']}") 
            num = int(input("Enter task number to complete:")) 
            if 1 <= num <= len(todos): 
                todos[num - 1]["done"] = True
                print(f"Task completed: {todos[num - 1]['task']}") 
    elif choice == "4": 
        if len(todos) == 0: 
            print("No task yet!") 
        else: 
            for i, todo in enumerate(todos): 
                print(f"{i + 1}. {todo['task']}") 
            num = int(input("Enter task number to delete:")) 
            if 1 <= num <= len(todos): 
                removed = todos.pop(num - 1) 
                print(f"Deleted: {removed['task']}") 
    elif choice == "5": 
        print("Goodbye!") 
        break 
    else: 
        print("Invalid choice!") 