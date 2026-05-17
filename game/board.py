from game.enums import GameState
from game.enums import Player


class Board :
    def __init__(self) :
        # each state is a list of 9 values, 3x3 matrix in a linear layout
        self.board_state = [None] * 9
        self.win_states = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]

    # Checks the state of the board - player 1 win, player 2 win, draw, or ongoing
    def check_state(self) :
        if self.is_winning_state(Player.PLAYER_1.value) :
            return GameState.PLAYER_1_WIN
        elif self.is_winning_state(Player.PLAYER_2.value) :
            return GameState.PLAYER_2_WIN
        elif self.is_full() :
            return GameState.DRAW
        else :
            return GameState.ONGOING
        
    # Checks if the board is empty - for initialization testing
    def is_empty(self) :
        return all(x is None for x in self.board_state)
    
    # Check if the board is full - done after win check to ensure DRAW
    def is_full(self) :
        return all(x is not None for x in self.board_state)
    
    # Compare board with game states to decide if player won
    def is_winning_state(self, player) :
        return any(all(self.board_state[x] == player for x in state) for state in self.win_states)
    
    def make_move(self, index, player) :
        if 0 <= index <= 8 and self.board_state[index] is None:
            self.board_state[index] = player
            return True
        return False
    
    def undo_move(self, index) :
        self.board_state[index] = None
    
    def available_moves(self) :
        return [i for i, val in enumerate(self.board_state) if val is None]