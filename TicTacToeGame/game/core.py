import helpers

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

def play_game(board_size, player1, player2):
    is_draw = True
    rounds = board_size * board_size
    current_player = player1
    board = helpers.make_board(board_size)
    print(format_board(board))
    
    for _ in range(rounds):
        play_move(board, current_player)
        
        if helpers.winner(board):
            helpers.print_winner(current_player)
            is_draw = False
            break
        
        if current_player == player1:
            current_player = player2
        elif current_player == player2:
            current_player = player1
    if is_draw:            
        helpers.print_draw()

play_game(helpers.BOARDSIZE,helpers.PLAYER1,helpers.PLAYER2)