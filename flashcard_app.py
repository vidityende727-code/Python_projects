flashcards = [] 
while True: 
    print("\n--- Flashcard App ---") 
    print("1. Add flashcard") 
    print("2. Study flashcards") 
    print("3. View all flashcards") 
    print("4. Delete flashcard") 
    print("5. Quit") 
    choice = input("\nEnter choice(1-5):") 
    if choice == "1": 
        question = input("Enter question:") 
        answer = input("Enter answer:") 
        flashcards.append({"question": question, "answer": answer}) 
        print("Flashcard added!") 
    elif choice == "2": 
        if len(flashcards) == 0: 
            print("No flashcards yet!") 
        else: 
            score = 0 
            for i, card in enumerate(flashcards): 
                print(f"\nCard {i + 1}: {card['question']}") 
                input("Press enter to see answer...") 
                print(f"Answer: {card['answer']}") 
                correct = input("Did you get it right? (y/n):").lower() 
                if correct == "y": 
                    score += 1 
            print(f"\nScore:{score}/{len(flashcards)}") 
    elif choice == "3": 
        if len(flashcards) == 0: 
            print("No flashcards yet!") 
        else: 
            print("\nAll flashcards:") 
            for i, card in enumerate(flashcards): 
                print(f"{i + 1}. Q: {card['question']}, A: {card['answer']}") 
    elif choice == "4": 
        if len(flashcards) == 0: 
            print("No flashcards yet!") 
        else: 
            for i, card in enumerate(flashcards): 
                print(f"{i + 1}. {card['question']}") 
                num = int(input("Enter card number to delete:")) 
                if 1 <= num <= len(flashcards): 
                    removed = flashcards.pop(num - 1) 
                    print(f"Deleted: {removed['question']}") 
    elif choice == "5": 
        print("Goodbye!") 
        break 
    else: 
        print("Invalid choice!")
                        