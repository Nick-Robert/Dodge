import pygame
from pygame.sprite import Sprite
import random


class Blue(Sprite):
    def __init__(self, ai_settings, screen):
        super(Blue, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load_basic('images/blue_box.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(40, 960)
        self.rect.y = random.randint(-100, 0)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.ai_settings.blue_speed_factor
        self.rect.y = self.y
        if self.rect.y >= 600:
            self.kill()

