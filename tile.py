import pygame
import config
import source


class OldTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.collideable = True

    def render(self):
        pygame.draw.rect(config.surface, (0, 255, 0), (self.x * config.tile_size, self.y * config.tile_size, config.tile_size, config.tile_size))


class Tile:
    def __init__(self, x, y, image, collideable):
        self.x = x
        self.y = y

        self.image = image
        self.collideable = collideable

    def interact(self):
        if self.collideable is True:
            self.collideable = False
        elif self.collideable is False:
            self.collideable = True

    def rect(self):
        return pygame.Rect(self.x * config.tile_size, self.y * config.tile_size, config.tile_size, config.tile_size)


class TileSet:
    def __init__(self, file):
        self.tiles = [[]]

        for i in range(config.map_x):  # generates empty collision map to be populated by update_map method
            self.tiles.append([])
            for j in range(config.map_y):
                self.tiles[i].append(None)

        self.load(file)

    def interact(self, x, y):
        self.tiles[x][y].interact()

    def render(self):
        for i in self.tiles:
            for j in i:
                if j:
                    print(j)
                    config.surface.blit(j.image, j.rect())

    def load(self, file):  # loads a map from a text file
        file = open(file)
        text = file.read()
        file.close()

        text_y = text.splitlines()

        x_cursor, y_cursor = 0, 0

        for y in text_y:
            text_x = list(y)
            x_cursor = 0

            for x in text_x:
                if x == "#":
                    self.tiles[x_cursor][y_cursor] = Tile(x_cursor, y_cursor, source.test_img, True)

                x_cursor += 1
            y_cursor += 1

        print(self.tiles)



# class TileSet:
#     def __init__(self, x, y, file):
#         self.tiles = []
#         self.collision_map = [[]]
#         self.x_limit = x
#         self.y_limit = y
#
#         for i in range(self.x_limit):  # generates empty collision map to be populated by update_map method
#             self.collision_map.append([])
#             for j in range(self.y_limit):
#                 self.collision_map[i].append(False)
#
#         self.update_map()
#
#         self.load(file)
#
#     def load(self, file):  # loads a map from a text file
#         file = open(file)
#         text = file.read()
#         file.close()
#
#         text_y = text.splitlines()
#
#         x_cursor, y_cursor = 0, 0
#
#         for y in text_y:
#             text_x = list(y)
#             x_cursor = 0
#
#             for x in text_x:
#                 if x == "#":
#                     self.tiles.append(Tile(x_cursor, y_cursor))
#
#                 x_cursor += 1
#             y_cursor += 1
# #
#     def update_map(self):  # updates collision map to reflect tile data
#         for i in self.tiles:
#             self.collision_map[i.x][i.y] = i.collideable
#
#     def render(self):
#         for i in self.tiles:
#             i.render()
