from Game.Tiles import Tile
from Game.Shared import *


class WallTile(Tile):

    def __init__(self, position, sprite, game):
        super(WallTile, self).__init__(position, sprite, game)
