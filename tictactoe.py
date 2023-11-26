def print_game_board(game_board):
    for board_row in game_board:
        print("|".join(board_row))
        print("-----")

def check_winner(game_board):
    # Check board_rows
    for board_row in game_board:
        if board_row[0] == board_row[1] == board_row[2] and board_row[0] != ' ':
            return True

    # Check columns
    for board_col in range(3):
        if game_board[0][board_col] == game_board[1][board_col] == game_board[2][board_col] and game_board[0][board_col] != ' ':
            return True

    # Check diagonals
    if game_board[0][0] == game_board[1][1] == game_board[2][2] and game_board[0][0] != ' ':
        return True
    if game_board[0][2] == game_board[1][1] == game_board[2][0] and game_board[0][2] != ' ':
        return True

    return False

def is_game_board_full(game_board):
    for board_row in game_board:
        for board_cell in board_row:
            if board_cell == ' ':
                return False
    return True

def tic_tac_toe():
    game_board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_game_board(game_board)
        # Check for exception if input is no a value that can be parsed to an int
        try:            
            board_row = int(input(f"Enter the row (0, 1, or 2) for {current_player}: "))
        except ValueError:
            print(f"Please input a number")
            continue
        try:
            board_col = int(input(f"Enter the column (0, 1, or 2) for {current_player}: "))
        except ValueError:
            print(f"Please input a number")
            continue
        
        # Check for exception if number is not in the range of 0, 1 and 2
        try:
            if game_board[board_row][board_col] == ' ':
                game_board[board_row][board_col] = current_player

                if check_winner(game_board):
                    print_game_board(game_board)
                    print(f"{current_player} wins!")
                    break
                elif is_game_board_full(game_board):
                    print_game_board(game_board)
                    print("It's a tie!")
                    break
                else:
                    current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("Cell already occupied. Try again.")
        except IndexError:
            print(f"Please only use 0, 1 or 2")


if __name__ == "__main__":
    tic_tac_toe()
