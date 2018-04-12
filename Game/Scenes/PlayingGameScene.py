import pygame
from Game.Scenes import Scene
from Game.Shared import *


class PlayingGameScene(Scene):

    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)
        self.__debugCount = 0
        self.__move_right = 1
        self.__move_left = 2
        self.__direction = 0

    def render(self):
        super(PlayingGameScene, self).render()

        game = self.get_game()
        level = game.get_level()
        player = game.get_player()
        player_position = game.get_player().get_position()
        move_right = self.__move_right
        move_left = self.__move_left
        direction = self.__direction

        for tile in game.get_level().get_tiles():
            if not tile.is_destroyed():
                game.screen.blit(tile.get_sprite(), tile.get_position())

        player.set_position((GameConstants.TILE_SIZE[0],
                             GameConstants.SCREEN_SIZE[1] - (GameConstants.TILE_SIZE[1] + GameConstants.PLAYER_SIZE[1])))

        if direction == move_right:
            player.set_position(
                (player_position[0] + 1, player.get_position()[1])
            )
            print(player.get_position())
        elif direction == move_left:
            player.set_position(
                (player_position[0] - 1, player.get_position()[1])
            )
            print(player.get_position())

        player.update_position()
        game.screen.blit(player.get_sprite(), player.get_position())

        while self.__debugCount == 0:
            print(player.get_position())
            self.__debugCount += 1

    def handle_events(self, events):
        super(PlayingGameScene, self).handle_events(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.__direction = self.__move_right
                elif event.key == pygame.K_a:
                    self.__direction = self.__move_left
            # elif event.type == pygame.KEYUP:
            #     if event.key == pygame.K_a:
            #         self.__direction = 0
            #     elif event.key == pygame.K_d:
            #         self.__direction = 0
