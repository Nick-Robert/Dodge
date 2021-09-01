import pygame


class Timer:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = 200
        self.height = 50
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.font = pygame.font.Font(None, 40)
        self.white = pygame.Color('white')

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def timer_func(self, start, end):
        txt = self.font.render(str(round(end - start, 2)), True, self.white)
        self.screen.blit(txt, (self.rect.centerx, self.rect.centery + 100))
        pygame.display.flip()
