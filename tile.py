import pygame
import config


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.collideable = True

    def render(self):
        pygame.draw.rect(config.surface, (0, 255, 0), (self.x * config.tile_size, self.y * config.tile_size, config.tile_size, config.tile_size))


class TileSet:
    def __init__(self, x, y):
        self.tiles = []
        self.collision_map = [[]]
        self.x_limit = x
        self.y_limit = y

        for i in range(self.x_limit):
            self.collision_map.append([])
            for j in range(self.y_limit):
                self.collision_map[i].append(False)

        self.update_map()

        self.load()

    def load(self):
        file = open('map_test')
        text = file.read()
        file.close()

        text_y = text.splitlines()

        x_cursor, y_cursor = 0, 0

        for y in text_y:
            text_x = list(y)
            x_cursor = 0

            for x in text_x:
                print(x, (x_cursor, y_cursor))

                if x == "#":
                    self.tiles.append(Tile(x_cursor, y_cursor))

                x_cursor += 1
            y_cursor += 1

    def update_map(self):
        for i in self.tiles:
            print(i.x, i.y)
            self.collision_map[i.x][i.y] = i.collideable

    def render(self):
        for i in self.tiles:
            i.render()
