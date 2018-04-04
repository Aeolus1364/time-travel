import pygame
import config
import tile


class TimeZone:
    def __init__(self):
        self.tileset = tile.TileSet('map_test')

    def render(self):
        self.tileset.update_map()
        self.tileset.render()

    def collision(self, x, y):
        return self.tileset.collision_map[x][y]

past = TimeZone()
present = TimeZone()
