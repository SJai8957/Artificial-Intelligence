#WAP to implement Tic-Tac-Toe Game using Python.

# Tic-Tac-Toe game implementation in Python

def print_board(board):
    """Function to display the Tic-Tac-Toe board"""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Check if a player has won"""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    """Check if the board is full (draw)"""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """Main function to play Tic-Tac-Toe"""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player = players[turn % 2]
        print(f"Player {player}'s turn.")

        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter col (0, 1, 2): "))
        except ValueError:
            print("Invalid input! Please enter numbers between 0 and 2.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid move! Row and column must be 0, 1, or 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Place move
        board[row][col] = player
        print_board(board)

        # Check for winner
        if check_winner(board, player):
            print(f"🎉 Player {player} wins!")
            break

        # Check for draw
        if is_full(board):
            print("It's a draw!")
            break

        turn += 1

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
