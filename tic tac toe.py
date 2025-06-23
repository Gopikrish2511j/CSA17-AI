board = [' ' for _ in range(9)]
def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print("\n")
def check_winner(player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]             
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False
def is_draw():
    return all(cell != ' ' for cell in board)
def play_game():
    current_player = 'X'
    while True:
        print_board()
        move = input(f"Player {current_player}, enter your move (1-9): ")
        if not move.isdigit() or not (1 <= int(move) <= 9):
            print("Invalid input. Try again.")
            continue
        move = int(move) - 1
        if board[move] != ' ':
            print("Cell already taken. Try again.")
            continue
        board[move] = current_player
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        elif is_draw():
            print_board()
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'
play_game()