import pygame
from settings import Settings
from Exc.game_stats import GameStats
from Exc.red_box import Red
import Exc.game_functions as gf
from pygame.sprite import Group
from Exc.button import Button
from Exc.timer import Timer

# Arrow keys to move, can go up, down, left, and right. Timer displays at the end of each attempt.


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
    timer = Timer(screen)
    pygame.display.set_caption("Dodge")
    red = Red(ai_settings, screen)
    blue = Group()
    counter = 0
    while True:
        gf.check_events(red, blue, stats, play_button)
        if stats.game_active:
            counter += 1
            red.update()
            if (counter / ai_settings.blue_spawn_rate).is_integer():
                gf.check_blue_spawn(ai_settings, screen, blue)
            gf.update_blue(ai_settings, red, blue, stats)
        gf.update_screen(ai_settings, screen, red, blue, stats, play_button, timer)

run_game()
