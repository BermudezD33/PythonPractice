PLAYER1 = 'X'
PLAYER2 = 'O'
print('Choose the size of the board: ')
BOARDSIZE = int(input())
print(f"The board is: {BOARDSIZE} x {BOARDSIZE}")
def print_winner(player):
    print(f'{player} wins!')

def print_draw():
    print("It's a draw!")

def make_board(size):
    return [[' '] * size for _ in range(size)]

def winning_line(strings):
    strings = set(strings)
    return len(strings) == 1 and ' ' not in strings

def row_winner(board):
    return any(winning_line(row) for row in board)

def column_winner(board):
    return row_winner(zip(*board))

def main_diagonal_winner(board):
    return winning_line(row[i] for i, row in enumerate(board))

def diagonal_winner(board):
    return main_diagonal_winner(board) or main_diagonal_winner(reversed(board))

def winner(board):
    return row_winner(board) or column_winner(board) or diagonal_winner(board)