from pygame.sprite import Group
import pygame, sys
import game_function as g_f
from char import Braum
from settings import Settings
#from background import Background
def init_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screan_width, game_settings.screan_height))
    ship=Braum(screen)
    #background=Background(screen)

    pygame.display.set_caption("Adventures of Braum and Pengui")
    while True:
        g_f.check_events(game_settings,screen,ship)
        g_f.update_screen(screen,ship)
        ship.update()
init_game()