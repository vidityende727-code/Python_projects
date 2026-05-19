contacts = {} 
while True: 
    print("\n--- Contact Book ---") 
    print("1. Add contact") 
    print("2. View all contacts") 
    print("3. Search contact") 
    print("4. Delete contact") 
    print("5. Quit") 
    choice = input("\nEnter choice (1-5):") 
    if choice == "1": 
        name = input("Enter name:").lower() 
        phone = input("Enter phone number:") 
        email = input("Enter email:") 
        contacts[name] = {"phone": phone, "email": email} 
        print(f"Contact added: {name}") 
    elif choice == "2": 
        if len(contacts) == 0: 
            print("No contacts yet!") 
        else: 
            print("\nAll contacts:") 
            for name, info in contacts.items(): 
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}") 
    elif choice == "3": 
        name = input("Enter name to search:").lower() 
        if name in contacts: 
            print(f"Name: {name}") 
            print(f"Phone: {contacts[name]['phone']}")  
            print(f"Email: {contacts[name]['email']}") 
        else: 
            print(f"{name} not found") 
    elif choice == "4": 
        name = input("Enter name to delete:").lower()  
        if name in contacts: 
            del contacts[name] 
            print(f"Deleted: {name}") 
        else: 
            print(f"{name} not found") 
    elif choice == "5": 
        print("Goodbye!") 
        break 
    else: 
        print("Invalid choice!") 
