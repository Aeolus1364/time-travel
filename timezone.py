import pygame
import config
import tile


class TimeZone:
    def __init__(self):
        self.tileset = tile.TileSet('map_test')

    def render(self):
        self.tileset.render()

    def collision(self, x, y):
        if self.tileset.tiles[x][y]:
            return self.tileset.tiles[x][y].collideable
        else:
            return False

    def interact(self, x, y):
        self.tileset.interact(x, y)

past = TimeZone()
present = TimeZone()
