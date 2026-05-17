from game.enums import Player

DISPLAY = {Player.PLAYER_1.value : 'X', Player.PLAYER_2.value : 'O', None: ' '}

def display_board(game_board) :
    print("------------ BOARD ------------")
    for i in range(3) :
        row = ' | '.join(DISPLAY[game_board.board_state[(3*i)+j]] for j in range(3))
        print(row)      
        if i < 2 :
            print('-' * 9)


