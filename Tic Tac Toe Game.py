# Tic Tac Toe Game.
# Define the main function with the player and board.
def main():
    player = next_player("")
    board = create_board()
    while not (winner(board) or draw_board(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print("End Of Game. Thanks for playing.")

# Create the board.
def create_board():
    board = []
    for sqaure in range(9):
        board.append(sqaure + 1)
    return board

# Display the board.
def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

# Define the draw board function.
def draw_board(board):
    for square in range(9):
        if board[square] != "X" and board[square] != "O":
            return False
        return True

# Define the winner function.
def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

# Define the make move function.
def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

# Define the next player function.
def next_player(current):
    if current == "" or current == "O":
        return "X"
    elif current == "X":
        return "O"

# Return the main function.
if __name__ == "__main__":
    main()