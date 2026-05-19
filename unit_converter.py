def format_num(n): 
    return int(n) if n == int(n) else round(n,2) 
while True: 
    print("\n--- Unit Converter ---") 
    print("1. Kilometers to Miles") 
    print("2. Miles to Kilometers") 
    print("3. Celsius to Fahrenheit") 
    print("4. Fahrenheit to Celsius") 
    print("5. Kilograms to Pounds") 
    print("6. Pounds to Kilograms") 
    print("7. Quit") 
    choice = input("\nEnter choice (1-7):") 
    if choice == "7": 
        print("Goodbye!") 
        break 
    value = float(input("Enter value:")) 
    dv = format_num(value)  
    if choice == "1": 
        print(f"{dv} km = {format_num(value * 0.621371)} miles") 
    elif choice == "2": 
        print(f"{dv} miles = {format_num(value / 0.621371)} km") 
    elif choice == "3": 
        print(f"{dv} C = {format_num((value * 9/5) + 32)} F") 
    elif choice == "4": 
        print(f"{dv} F = {format_num((value - 32) * 5/9)} C") 
    elif choice == "5": 
        print(f"{dv} kg = {format_num(value * 2.20462)}pounds") 
    elif choice == "6": 
        print(f"{dv} pounds = {format_num(value / 2.20462)} kg") 
    else: 
        print("Invalid choice!") 


