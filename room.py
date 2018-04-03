import pygame
import config
import tile


class Map:
    def __init__(self):
        self.tileset = tile.TileSet(10, 10)

    def update(self):
        self.tileset.update_map()
        self.tileset.render()

    def collision(self, x, y):
        return self.tileset.collision_map[x][y]


past = Map()
present = Map()
