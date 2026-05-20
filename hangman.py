import random 
words = ["python", "programming", "computer", "keyboard", "monitor", "software", "developer", "function", "variable", "loop"] 
word = random.choice(words) 
guessed = [] 
attempts = 6 
print("Welcome to Hangman!") 
while attempts > 0: 
    display = "" 
    for letter in word: 
        if letter in guessed: 
            display += letter + " " 
        else: 
            display += "_" 
    print(f"\nWord: {display}") 
    print(f"Guessed: {guessed}") 
    print(f"Attempts left: {attempts}") 
    if "_" not in display: 
        print(f"You won! The word was: {word} 🎉") 
        break 
    guess = input("Guess a letter:").lower() 
    if len(guess)!= 1: 
        print("Enter only one letter!") 
    elif guess in guessed: 
        print("Already guessed!") 
    elif guess in word: 
        guessed.append(guess) 
        print("Correct!") 
    else: 
        guessed.append(guess) 
        attempts -= 1 
        print(f"Wrong! {attempts} attempts left.") 
else: 
    print(f"Game Over! The word was: {word} 😢") 