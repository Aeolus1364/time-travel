import pygame
import tile
import config
import math
import timezone


class Player:
    def __init__(self):
        self.x = 0  # position in terms of tiles
        self.y = 4
        self.direction = "none"
        self.next_direction = "none"
        self.pos_x = 0  # pixel position for rendering
        self.pos_y = 256
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 8
        self.distance = 0

    def update_pos(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

    def change_direction(self, direction):
        if self.direction == "none":
            self.direction = direction
        else:
            self.next_direction = direction

    def cancel_direction(self, direction):
        if direction == self.next_direction:
            self.next_direction = "none"

    def update_movement(self, direction_pressed):
        if self.direction == "up":
            self.vel_y = -self.speed
            if self.pos_y % config.tile_size == 0:  # if player is on a tile
                if direction_pressed != "up":  # if direction changes, stop velocity, and start next direction
                    self.direction = self.next_direction
                    self.vel_y = 0
                if timezone.present.collision(self.x, self.y - 1) is True:  # if collision occurs, stop velocity, start next direction
                    self.direction = self.next_direction
                    self.vel_y = 0

        elif self.direction == "down":
            self.vel_y = self.speed
            if self.pos_y % config.tile_size == 0:
                if direction_pressed != "down":
                    self.direction = self.next_direction
                    self.vel_y = 0
                if timezone.present.collision(self.x, self.y + 1) is True:
                    self.direction = self.next_direction
                    self.vel_y = 0

        elif self.direction == "left":
            self.vel_x = -self.speed
            if self.pos_x % config.tile_size == 0:
                if direction_pressed != "left":
                    self.direction = self.next_direction
                    self.vel_x = 0
                if timezone.present.collision(self.x - 1, self.y) is True:
                    self.direction = self.next_direction
                    self.vel_x = 0

        elif self.direction == "right":
            self.vel_x = self.speed
            if self.pos_x % config.tile_size == 0:
                if direction_pressed != "right":
                    self.direction = self.next_direction
                    self.vel_x = 0
                if timezone.present.collision(self.x + 1, self.y) is True:
                    self.direction = self.next_direction
                    self.vel_x = 0

        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

        self.x = round(self.pos_x / config.tile_size)
        self.y = round(self.pos_y / config.tile_size)

    def render(self):
        pygame.draw.rect(config.surface, (0, 0, 0), (self.pos_x, self.pos_y, config.tile_size, config.tile_size))


player = Player()
