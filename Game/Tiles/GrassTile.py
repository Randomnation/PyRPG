from Game.Tiles import Tile
from Game.Shared import *


class GrassTile(Tile):

    def __init__(self, position, sprite, game):
        super(GrassTile, self).__init__(position, sprite, game)
