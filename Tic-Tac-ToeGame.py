def row_winner(board):
    for i in range(len(board)):
        first_space = None
        winner = True
        for j in range(len(board)):
            print(board[i][j])
            current_space = board[i][j]
            if first_space is None:
                first_space = current_space
            elif not first_space == current_space:
                winner = False
                break
            elif current_space == ' ':
                winner = False
                break     
        if winner:
            break    
    return winner


def column_winner(board):
    for i in range(len(board)):
        first_space = None
        winner = True
        for j in range(len(board)):
            print(board[j][i])
            current_space = board[j][i]
            if first_space is None:
                first_space = current_space
            elif not first_space == current_space:
                winner = False
                break
            elif current_space == ' ':
                winner = False
                break  
        if winner:
            break
    return winner


def diagonal_winner(board):
    first_space = None
    winner = True
    lenght = len(board)
    
    for i in range(lenght):
        print(board[i][i])
        current_space = board[i][i]
        if first_space is None:
            first_space = current_space
        elif not first_space == current_space:
            winner = False
            break
        elif current_space == ' ':
            winner = False
            break  
        
    if winner:
        return winner
        
    first_space = None
    winner = True
    for i in range(lenght):
        current_space = board[i][(lenght-1)-i]
        print(current_space)
        if first_space is None:
            first_space = current_space
        elif not first_space == current_space:
            winner = False
            break
        elif current_space == ' ':
            winner = False
            break  
        
    return winner



def winner(board):
    winner = False
    if row_winner(board):
        winner = True
    elif column_winner(board):
        winner = True
    elif diagonal_winner(board):
        winner = True
    return winner

def format_board(board):
    joined_rows = []
    board_lines = ''
    for _ in range(len(board)-1):
        if _ is 0:
            board_lines += '-'
        board_lines += '+-'
    
    for row in board:
        joined_rows.append('|'.join(row)) 
        joined_rows.append(board_lines)
    joined_rows.pop()
    
    print('\n'.join(joined_rows))
    return  '\n'.join(joined_rows)


#ver2
def format_board(board):
    joined_rows = []
    for row in board:
        joined_rows.append("".join(row))
    return "\n".join(joined_rows)






def format_board(board):
    first_row = ' '
    for i in range(len(board)):
        first_row += str(i + 1)
    joined_rows = [first_row]
    for i in range(len(board)):
        joined_row = str(i + 1) + ''.join(board[i])
        joined_rows.append(joined_row)
    return "\n".join(joined_rows)

def play_game():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]
    print(format_board(board))
    print('\nX to play:\n')
    play_move(board, 'X')
    print(format_board(board))
    print('\nO to play:\n')
    play_move(board, 'O')
    print(format_board(board))

def play_move(board, player):
   # x = int(input('\nEnter a number for the row:\n'))
   # y = int(input('\nEnter a number for the column:\n'))
    x = int(input()) -1
    y = int(input()) -1
    board[x][y] = player

play_game()




assert_equal(
    row_winner(
        [
            ['A', 'A', 'B', 'A'],
            [' ', ' ', ' ', ' '],
            ['A', ' ', ' ', 'A'],
            ['B', ' ', 'B', 'A']
        ]
    ),
    False
)
assert_equal(
    row_winner(
        [
            ['X', ' ', 'X'],
            ['O', 'X', 'X'],
            ['O', 'O', 'O']
        ]
    ),
    True
)
assert_equal(
    row_winner(
        [
            ['S', 'S', 'S', 'S'],
            ['M', 'M', 'S', ' '],
            [' ', 'S', 'M', 'S'],
            [' ', 'M', ' ', 'S']
        ]
    ),
    True
)

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

def format_board(board):
    size = len(board)
    line = f'\n  {"+".join("-" * size)}\n'
    rows = [f'{i + 1} {"|".join(row)}' for i, row in enumerate(board)]
    return f'  {" ".join(str(i + 1) for i in range(size))}\n{line.join(rows)}'

def play_move(board, player):
    print(f'{player} to play:')
    row = int(input()) - 1
    col = int(input()) - 1
    board[row][col] = player
    print(format_board(board))

def make_board(size):
    return [[' '] * size for _ in range(size)]

def print_winner(player):
    print(f'{player} wins!')

def print_draw():
    print("It's a draw!")

def play_game(board_size, player1, player2):
    is_draw = True
    rounds = board_size * board_size
    current_player = player1
    board = make_board(board_size)
    print(format_board(board))
    
    for _ in range(rounds):
        play_move(board, current_player)
        
        if winner(board):
            print_winner(current_player)
            is_draw = False
            break
        
        if current_player == player1:
            current_player = player2
        elif current_player == player2:
            current_player = player1
        
    if is_draw:            
        print_draw()

play_game(3, 'X', 'O')