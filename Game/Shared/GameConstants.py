import os


class GameConstants:
    SCREEN_SIZE = [800, 800]
    TILE_SIZE = [100, 100]
    PLAYER_SIZE = [90, 90]

    SPRITE_WALL = os.path.join("Game", "Assets", "wall_tile.png")
    SPRITE_GRASS = os.path.join("Game", "Assets", "grass_tile.png")
    SPRITE_PLAYER = os.path.join("Game", "Assets", "player_placeholder.png")
