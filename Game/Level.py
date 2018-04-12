import os
import fileinput
import pygame

from Game.Tiles import *
from Game.Shared.GameConstants import GameConstants


class Level:

    def __init__(self, game):
        self.__game = game
        self.__current_level = 0
        self.__tiles = []

    def get_tiles(self):
        return self.__tiles

    def load(self, level):
        self.__current_level = level
        self.__tiles = []

        x, y = 0, 0

        for line in fileinput.input(os.path.join("Game", "Assets", "Maps", "map" + str(level) + ".dat")):
            for current_tile in line:
                if current_tile == "0":
                    tile = Tile([x, y], pygame.image.load(GameConstants.SPRITE_GRASS), self.__game)
                    self.__tiles.append(tile)

                elif current_tile == "1":
                    tile = Tile([x, y], pygame.image.load(GameConstants.SPRITE_WALL), self.__game)
                    self.__tiles.append(tile)

                x += GameConstants.TILE_SIZE[0]

            x = 0
            y += GameConstants.TILE_SIZE[1]
