import random 
quotes = [ 
    {"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"}, 
    {"quote": "In the middle of every difficulty lies opportunity.", "author": "Albert Einstein"}, 
    {"quote": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"}, 
    {"quote": "Life is what happens when you are busy making other plans.", "author": "Jhon Lennon"}, 
    {"quote": "The future belong to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"}, 
    {"quote": "Success is not final, failure is not fatal, it is the courage to continue that counts.", "author": "Winston Churchill"}, 
    {"quote": "You miss 100% of the shots you dont take.", "author": "Wayne Gretzky"}, 
    {"quote": "Whether you think you can or think you cant, you are right.", "author": "Henry Ford"}, 
    {"quote": "The best time to plant a tree was 20 years ago.The second best time is now.", "author": "Chinese Proverb"}, 
    {"quote": "An unexamined life is not worth living.", "author": "Socrates"}
] 
while True: 
    print("\n--- Random Quote Generator ---") 
    print("1. Get random quote") 
    print("2. Get quote by number") 
    print("3. View all quotes") 
    print("4. Quit") 
    choice = input("\nEnter choice (1-4): ") 
    if choice == "1": 
        q = random.choice(quotes) 
        print(f'\n"{q["quote"]}\"')   
        print(f"- {q['author']}") 
    elif choice == "2":  
        print(f"Enter number (1-{len(quotes)}):", end ="") 
        num = int(input()) 
        if 1 <= num <= len(quotes): 
            q = quotes[num-1] 
            print(f'\n\"{q["quote"]}\"') 
            print(f"- {q['author']}") 
        else: 
            print("Invalid number!") 
    elif choice == "3": 
        print("\nAll quotes:") 
        for i, q in enumerate(quotes): 
            print(f'\n{i + 1}.\"{q["quote"]}\"')   
            print(f"- {q['author']}") 
    elif choice == "4": 
        print("Goodbye!") 
        break 
    else: 
        print("Invalid choices!") 

    