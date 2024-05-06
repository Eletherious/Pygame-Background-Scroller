import pygame
import os


class BackgroundLayer:
    def __init__(self, image_path, speed, window_width, window_height):
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("assets", image_path)),
                                            (window_width, window_height))
        self.speed = speed
        self.width = self.image.get_width()
        self.x_position = 0

    def move(self):
        self.x_position -= self.speed
        if self.x_position < -self.width:
            self.x_position = 0

    def draw(self, window):
        window.blit(self.image, (self.x_position, 0))
        if self.x_position < 0:
            window.blit(self.image, (self.x_position + self.width, 0))
