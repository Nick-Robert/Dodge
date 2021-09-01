import sys
import pygame
from Exc.blue_box import Blue
import time


start = 0
end = 0


def check_events(red, blue, stats, play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                red.moving_right = True
            elif event.key == pygame.K_LEFT:
                red.moving_left = True
            elif event.key == pygame.K_UP:
                red.moving_up = True
            elif event.key == pygame.K_DOWN:
                red.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                red.moving_right = False
            elif event.key == pygame.K_LEFT:
                red.moving_left = False
            elif event.key == pygame.K_UP:
                red.moving_up = False
            elif event.key == pygame.K_DOWN:
                red.moving_down = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, red, blue, mouse_x, mouse_y)


def check_play_button(stats, play_button, red, blue, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        pygame.mouse.set_visible(False)
        stats.game_active = True
        global start
        start = get_start()
        red.center_red()
        blue.empty()


def update_screen(ai_settings, screen, red, blue, stats, play_button, timer):
    screen.fill(ai_settings.bg_color)
    red.blitme()
    blue.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
        start_end_time(stats, timer)
    pygame.display.flip()


def update_blue(ai_settings, red, blue, stats):
    collisions = pygame.sprite.spritecollideany(red, blue)
    ai_settings.blue_speed_factor += .00009
    if (ai_settings.blue_spawn_rate / 7700).is_integer():
        ai_settings.blue_spawn_rate -= 2
    if collisions:
        game_over(stats, ai_settings)
    blue.update()


def check_blue_spawn(ai_settings, screen, blue):
    if len(blue) < ai_settings.blue_boxes_allowed:
        blue.add(Blue(ai_settings, screen))


def game_over(stats, ai_settings):
    stats.game_active = False
    pygame.mouse.set_visible(True)
    ai_settings.blue_speed_factor = .5
    ai_settings.blue_spawn_rate = 40
    global end
    end = get_end()


def start_end_time(stats, timer):
    if stats.game_active:
        return
    timer.timer_func(start, end)


def get_start():
    global start
    start = time.time()
    return start


def get_end():
    global end
    end = time.time()
    return end
