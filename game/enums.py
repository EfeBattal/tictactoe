from enum import Enum

class GameState(Enum) :
    PLAYER_1_WIN = 1
    PLAYER_2_WIN = 2
    DRAW = 3
    ONGOING = 4

class Player(Enum) :
    PLAYER_1 = 1
    PLAYER_2 = -1
