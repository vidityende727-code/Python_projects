def print_board(board): 
    print("\n") 
    print(f" {board[0]}, {board[1]}, {board[2]}") 
    print("---,---,---") 
    print(f" {board[3]}, {board[4]}, {board[5]}") 
    print("---,---,---") 
    print(f" {board[6]}, {board[7]}, {board[8]}") 
    print("\n") 
def check_winner(board,player): 
    wins = [ 
        [0,1,2], [3,4,5], [6,7,8], 
        [0,3,6], [1,4,7], [2,5,8], 
        [0,4,8], [2,4,6] 
    ] 
    for combo in wins: 
        if all(board[i] == player for i in combo): 
            return True 
    return False 
board = ["1","2","3","4","5","6","7","8","9"] 
current = "X" 
print("Tic Tac Toe!") 
print("Choose position 1-9") 
while True: 
    print_board(board) 
    move = input(f"Player {current}, enter position(1-9):")  
    if not move.isdigit() or int(move) < 1 or int(move) > 9: 
        print("Invalid move!") 
        continue 
    pos = int(move) - 1 
    if board[pos] == "X" or board[pos] == "O": 
        print("Position taken!") 
        continue 
    board[pos] = current 
    if check_winner(board,current): 
        print_board(board) 
        print(f"Player {current} wins!") 
        break 
    if all(cell == "X" or cell == "O" for cell in board): 
        print_board(board) 
        print("Its a draw!") 
        break 
    current = "O" if current == "X" else "X"  
     