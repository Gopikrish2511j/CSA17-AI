import math

HUMAN = 'O'
AI = 'X'
EMPTY = ' '

board = [[EMPTY for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def is_moves_left(board):
    return any(cell == EMPTY for row in board for cell in row)

def evaluate(board):
    for row in board:
        if row.count(AI) == 3:
            return +10
        if row.count(HUMAN) == 3:
            return -10
    for col in range(3):
        if all(board[row][col] == AI for row in range(3)):
            return +10
        if all(board[row][col] == HUMAN for row in range(3)):
            return -10
    if all(board[i][i] == AI for i in range(3)):
        return +10
    if all(board[i][i] == HUMAN for i in range(3)):
        return -10
    if all(board[i][2 - i] == AI for i in range(3)):
        return +10
    if all(board[i][2 - i] == HUMAN for i in range(3)):
        return -10
    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10 or score == -10:
        return score
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = EMPTY
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = EMPTY
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                move_val = minimax(board, 0, False)
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

def play_game():
    print("Tic Tac Toe (You are O, AI is X)")
    print_board(board)

    while is_moves_left(board):
        # Human move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] != EMPTY:
            print("Invalid move! Try again.")
            continue
        board[row][col] = HUMAN
        print_board(board)

        if evaluate(board) == -10:
            print("You win!")
            return

        if not is_moves_left(board):
            print("It's a draw!")
            return

        # AI move
        print("AI is making a move...")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = AI
        print_board(board)

        if evaluate(board) == 10:
            print("AI wins!")
            return

    print("It's a draw!")

# Start game
play_game()
