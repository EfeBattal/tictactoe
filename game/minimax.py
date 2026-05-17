from game.enums import GameState

def minimax(game_board, is_maximizing) :
    # where board is the Board object and is_maximizing = 1 means AI
    state = game_board.check_state()
    # base case
    if(state == GameState.PLAYER_1_WIN) :
        return 1
    elif(state == GameState.PLAYER_2_WIN) :
        return -1
    elif(state == GameState.DRAW) :
        return 0
    
    # recursive case
    player = 1 if is_maximizing else -1
    moves = game_board.available_moves()
    results = []
    for move in moves :
        game_board.make_move(move, player)
        results.append(minimax(game_board, not is_maximizing))
        game_board.undo_move(move)
    return max(results) if is_maximizing else min(results)

    
def best_move(game_board, player) :
    moves = game_board.available_moves()
    best_move = None
    best = -2 if player == 1 else 2
    is_maximizing = player == 1
    for move in moves :
        game_board.make_move(move, player)
        result = minimax(game_board, not is_maximizing)
        game_board.undo_move(move)
        if is_maximizing and result > best or not is_maximizing and result < best:
            best_move = move
            best = result
    return best_move