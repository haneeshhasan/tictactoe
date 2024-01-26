def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        row = int(input("Enter row (0, 1, or 2) for player {}: ".format(players[current_player])))
        col = int(input("Enter column (0, 1, or 2) for player {}: ".format(players[current_player])))

        if board[row][col] == " ":
            board[row][col] = players[current_player]

            if check_winner(board, players[current_player]):
                print_board(board)
                print("Player {} wins!".format(players[current_player]))
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            else:
                current_player = (current_player + 1) % 2
        else:
            print("That position is already taken. Try again.")

if __name__ == "__main__":
    main()
