from game.board import Board
from game.display import display_board
from game.minimax import best_move
from game.enums import GameState
from game.enums import Player

def main() :
    board = Board()
    state = GameState.ONGOING
    while(state == GameState.ONGOING) :
        display_board(board)
        human_move = int(input("What move would you like to do (1-9): ")) - 1
        board.make_move(human_move, Player.PLAYER_1.value)
        state = board.check_state()
        if(state == GameState.ONGOING) :
            ai_move = best_move(board, Player.PLAYER_2.value)
            board.make_move(ai_move, Player.PLAYER_2.value)
            state = board.check_state()

    print(state)

if __name__ == "__main__" :
    main()