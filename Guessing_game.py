import random 
number = random.randint(1,100) 
print("I have thought of a number between 1 and 100!") 
attempts = 0 
max_attempts = 7
while attempts < max_attempts: 
    guess = int(input(f"Enter your guess ({attempts + 1}/{max_attempts}):")) 
    attempts += 1 
    if guess == number: 
        print(f"Correct! You won!🎉 you guessed it in {attempts} attempts!") 
        break 
    elif guess < number: 
        print("Too low! Try a bigger number.") 
    else: 
        print("Too high! Try a smaller number.") 
else: 
    print(f"Game Over!😢 The number was {number}.") 

