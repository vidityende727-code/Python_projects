while True: 
    print("\n--- Calculator ---") 
    print("1.Add") 
    print("2.Subtract") 
    print("3.Multiply") 
    print("4.Divide") 
    print("5.Quit") 
    choice = input("\nEnter choice (1/2/3/4/5):") 
    if choice == "5": 
        print("Goodbye!") 
        break 
    num1 = float(input("Enter first number:")) 
    num2 = float(input("Enter second number:")) 
    if choice == "1": 
        result = num1 + num2 
        print(f"Result: {int(result) if result == int(result)else round(result, 10)}") 
    elif choice == "2": 
        result = num1 - num2 
        print(f"Result: {int(result) if result == int(result) else round(result, 10)}") 
    elif choice == "3": 
        result = num1 * num2 
        print(f"Result: {int(result) if result == int(result) else round(result, 10)}") 
    elif choice == "4": 
        if num2 == 0: 
            print("Error! Cannot divide by zero.") 
        else: 
            result = num1 / num2 
            print(f"Result: {int(result) if result == int(result) else round(result, 10)}") 
    else: 
        print("Invalid choice!")

