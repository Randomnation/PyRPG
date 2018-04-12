from Game.Shared import *


class Player(GameObject):

    def __init__(self, position, sprite):
        super(Player, self).__init__(position, GameConstants.PLAYER_SIZE, sprite)
        self.__increment = [2, 2]
        self.__direction = [1, 1]

    def set_position(self, position):

        new_position = [position[0], position[1]]
        size = self.get_size()

        if new_position[0] + size[0] > GameConstants.SCREEN_SIZE[0] - GameConstants.TILE_SIZE[0]:
            new_position[0] = GameConstants.SCREEN_SIZE[0] - GameConstants.TILE_SIZE[0]

        if new_position[1] + size[1] > GameConstants.SCREEN_SIZE[1] - GameConstants.TILE_SIZE[1]:
            new_position[1] = GameConstants.SCREEN_SIZE[1] - GameConstants.TILE_SIZE[1]

        super(Player, self).set_position(new_position)

    def update_position(self):

        position = self.get_position()
        size = self.get_size()

        new_position = [position[0] + (self.__increment[0]) * self.__direction[0],
                        position[1] + (self.__increment[1]) * self.__direction[1]]

        if new_position[0] + size[0] >= GameConstants.SCREEN_SIZE[0]:
            self.__direction[0] *= -1
            new_position = [GameConstants.SCREEN_SIZE[0] - size[0], new_position[1]]

        if new_position[0] <= 0:
            self.__direction[0] *= -1
            new_position = [0, new_position[1]]

        if new_position[1] + size[1] >= GameConstants.SCREEN_SIZE[1]:
            self.__direction[1] *= -1
            new_position = [new_position[0], GameConstants.SCREEN_SIZE[1] - size[1]]

        if new_position[1] <= 0:
            self.__direction[1] *= -1
            new_position = [new_position[0], 0]

        self.set_position(new_position)

