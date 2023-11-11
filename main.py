import os

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=' ')
            if j < 2:
                print('|', end=' ')
        print()
        if i < 2:
            print('-' * 9)

def player_input(board, player):
    while True:
        user_input = input(f"Player {player}, enter your move (row and column): ")
        try:
            row, col = map(int, user_input.split())
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter row and column as space-separated integers.")

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]):  # Check row
            return True
        if all(board[j][i] == player for j in range(3)):  # Check column
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True  # Check diagonals
    return False

def check_tie(board):
    return all(cell != ' ' for row in board for cell in row)

def switch_player(player):
    return 'X' if player == 'O' else 'O'

def main():
    board = initialize_board()
    player = 'X'  # X always goes first
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_board(board)
        player_input(board, player)
        if check_win(board, player):
            os.system('cls' if os.name == 'nt' else 'clear')
            print_board(board)
            print(f"Player {player} wins!")
            break
        if check_tie(board):
            os.system('cls' if os.name == 'nt' else 'clear')    
            print_board(board)
            print("It's a tie!")
            break
        player = switch_player(player)

main()