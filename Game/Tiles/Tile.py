from Game.Shared import GameObject
from Game.Shared import GameConstants


class Tile(GameObject):

    def __init__(self, position, sprite, game):
        self.__game = game
        self.__lives = 1
        super(Tile, self).__init__(position, GameConstants.TILE_SIZE, sprite)

    def get_game(self):
        return self.__game

    def is_destroyed(self):
        return self.__lives <= 0
