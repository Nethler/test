import pygame
class Braum():
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load("images/1.png")
        self.image = pygame.transform.scale(self.image, (125, 215))
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.centery=self.screen_rect.centery
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.space_center = False

    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left>self.screen_rect.left:
            self.rect.centerx -= 1
        if self.moving_up and self.rect.top>self.screen_rect.top:
            self.rect.centery -= 1
        if self.space_center:
            self.rect.centerx=self.screen_rect.centerx
            self.rect.centery = self.screen_rect.centery