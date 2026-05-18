while True: 
    print("\n--- BMI Calculator ---") 
    print("1. Calculate BMI") 
    print("2. Quit") 
    choice = input("\nEnter choice (1/2):") 
    if choice == "2": 
        print("Goodbye!") 
        break 
    name = input("Enter your name:") 
    weight = float(input("Enter your weight(kg):")) 
    height = float(input("Enter your height(meters):")) 
    bmi = weight / (height ** 2) 
    bmi = round(bmi,1) 
    print(f"\nHello {name}!") 
    print(f"Your BMI is: {bmi}") 
    if bmi < 18.5: 
        print("Category: Underweight") 
    elif bmi < 25: 
        print("Category: Normal weight") 
    elif bmi < 30: 
        print("Category: Overweight") 
    else: 
        print("Category: Obese") 
