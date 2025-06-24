import math

# Initialize the board
board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        print(board[i*3], "|", board[i*3+1], "|", board[i*3+2])
        if i < 2:
            print("--+---+--")

def check_winner(b, player):
    win_states = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(b[x] == b[y] == b[z] == player for x, y, z in win_states)

def minimax(b, is_max):
    if check_winner(b, "O"):
        return 1
    elif check_winner(b, "X"):
        return -1
    elif " " not in b:
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best = max(best, minimax(b, False))
                b[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                best = min(best, minimax(b, True))
                b[i] = " "
        return best

def best_move():
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            move_val = minimax(board, False)
            board[i] = " "
            if move_val > best_val:
                move = i
                best_val = move_val
    return move

# Game Loop
print("Tic-Tac-Toe! You are X, AI is O.")
while True:
    print_board()
    user_move = int(input("Enter position (0-8): "))
    if board[user_move] == " ":
        board[user_move] = "X"
    else:
        print("Invalid move!")
        continue

    if check_winner(board, "X"):
        print_board()
        print("You win!")
        break
    if " " not in board:
        print_board()
        print("It's a tie!")
        break

    ai = best_move()
    board[ai] = "O"
    if check_winner(board, "O"):
        print_board()
        print("AI wins!")
        break
