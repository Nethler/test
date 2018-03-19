import pygame, sys
from background import Background
def check_events(game_settings,screen,ship):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            check_keydown_events(game_settings,screen,i,ship)
        elif i.type == pygame.KEYUP:
            check_keyup_events(i, ship)

def update_screen(screen,ship):
    #background.update()
    ship.blitme()
    pygame.display.flip()


def check_keydown_events(game_settings,screen,i,ship):
    if i.key == pygame.K_LEFT:
        ship.moving_left = True
    elif i.key == pygame.K_RIGHT:
        ship.moving_right = True
    #elif i.key == pygame.K_SPACE:
        #ship.moving_up = True


def check_keyup_events(i,ship):
    if i.key == pygame.K_LEFT:
        ship.moving_left = False
    elif i.key == pygame.K_RIGHT:
        ship.moving_right = False
    #elif i.key == pygame.K_SPACE:
        #ship.moving_up = False