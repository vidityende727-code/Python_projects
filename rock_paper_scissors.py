import random 
choices =["rock", "paper", "scissors"] 
player_score = 0 
computer_score = 0 
while True: 
    computer = random.choice(choices) 
    player = input("\nEnter rock,paper, or scissors( or quit):").lower() 
    if player == "quit": 
        print(f"\nFinal score - You: {player_score} or computer: {computer_score}") 
        break 
    print(f"Computer chose: {computer}") 
    if player == computer: 
        print("Tie!") 
    elif(player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"): 
        print(f"You win! {player} beats {computer}!") 
        player_score += 1 
    else: 
        print(f"You lose! {computer} beats {player}!") 
        computer_score += 1 
    print(f"Score - You: {player_score} or computer: {computer_score}") 
       