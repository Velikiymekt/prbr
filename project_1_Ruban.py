import random

board = [" " for _ in range(9)]

def print_board():
    print("+" + "---+" * 3)
    for i in range(3):
        print("|", board[3 * i], "|", board[3 * i + 1], "|", board[3 * i + 2], "|")
        print("+" + "---+" * 3)

def check_win(player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for positions in win_positions:
        if all(board[pos] == player for pos in positions):
            return True
    return False

def check_draw():
    return all(cell != " " for cell in board)

board[4] = "X"

while True:
    print_board()
    while True:
        try:
            user_move = int(input("Enter your move (1-9): ")) - 1
            if user_move < 0 or user_move >= 9 or board[user_move] != " ":
                print("Invalid move, try again.")
            else:
                board[user_move] = "O"
                break
        except ValueError:
            print("Invalid input, enter a number between 1 and 9.")
    if check_win("O"):
        print_board()
        print("Congratulations! You win!")
        break
    if check_draw():
        print_board()
        print("It's a draw!")
        break
    while True:
        comp_move = random.randint(0, 8)
        if board[comp_move] == " ":
            board[comp_move] = "X"
            break

    if check_win("X"):
        print_board()
        print("Computer wins!")
        break
    if check_draw():
        print_board()
        print("It's a draw!")
        break