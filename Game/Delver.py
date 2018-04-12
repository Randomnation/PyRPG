import pygame

from Game import *
from Game.Scenes import *
from Game.Shared import GameConstants


class Delver:

    def __init__(self):
        self.__level = Level(self)
        self.__level.load(0)

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Delver - PyGame")

        self.__clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE,
                                              pygame.DOUBLEBUF, 32)

        self.__player = Player((GameConstants.SCREEN_SIZE[0]/2, GameConstants.SCREEN_SIZE[1]/2),
                               pygame.image.load(GameConstants.SPRITE_PLAYER),
                               )
        self.__scenes = (
            PlayingGameScene(self),
        )
        self.__current_scene = 0

    def start(self):
        while True:
            self.__clock.tick(100)
            self.screen.fill((0, 0, 0))

            current_scene = self.__scenes[self.__current_scene]
            current_scene.handle_events(pygame.event.get())
            current_scene.render()

            pygame.display.update()

    def get_level(self):
        return self.__level

    def get_player(self):
        return self.__player
