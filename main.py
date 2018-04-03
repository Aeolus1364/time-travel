import pygame
import player
import config
import tile
import room

pygame.init()

# pygame.display.set_caption()
# pygame.display.set_icon()


class Main:
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.running = True

        self.direction_pressed = "none"

    def game_loop(self):
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.direction_pressed = "up"
                        player.player.change_direction(self.direction_pressed)

                    if event.key == pygame.K_s:
                        self.direction_pressed = "down"
                        player.player.change_direction(self.direction_pressed)

                    if event.key == pygame.K_a:
                        self.direction_pressed = "left"
                        player.player.change_direction(self.direction_pressed)

                    if event.key == pygame.K_d:
                        self.direction_pressed = "right"
                        player.player.change_direction(self.direction_pressed)

                    if event.key == pygame.K_ESCAPE:
                        config.surface = pygame.display.set_mode((config.display_x, config.display_y))

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        if self.direction_pressed == "up":
                            self.direction_pressed = "none"
                        player.player.cancel_direction("up")

                    if event.key == pygame.K_s:
                        if self.direction_pressed == "down":
                            self.direction_pressed = "none"
                        player.player.cancel_direction("down")

                    if event.key == pygame.K_a:
                        if self.direction_pressed == "left":
                            self.direction_pressed = "none"
                        player.player.cancel_direction("left")

                    if event.key == pygame.K_d:
                        if self.direction_pressed == "right":
                            self.direction_pressed = "none"
                        player.player.cancel_direction("right")

            config.surface.fill((255, 255, 255))

            room.present.update()

            player.player.update_movement(self.direction_pressed)
            player.player.render()


            # print(player.player.pos_x, player.player.pos_y)
            # print(player.player.pos_x/global_vars.tile_size, player.player.pos_y/global_vars.tile_size)

            # print(self.direction_pressed, player.player.direction, player.player.next_direction)

            pygame.display.update()
            self.clock.tick(config.fps)
        pygame.quit()


game = Main()
game.game_loop()
