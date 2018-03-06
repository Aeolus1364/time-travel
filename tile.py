import pygame
import settings


class Tile:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.collideable = True

    def render(self):
        pygame.draw.rect(settings.surface, (0, 255, 0), (self.x * settings.tile_size, self.y * settings.tile_size, settings.tile_size, settings.tile_size))

