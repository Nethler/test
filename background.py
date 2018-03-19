import pygame
class Background():
    def __init__(self, screen):
        self.screen = screen
        self.bg_img = pygame.image.load("images/2.jpg").convert()
        self.rect_img = self.bg_img.get_rect()
        self.bg_speed = 0.2
        self.bg_y1 = 0
        self.bg_y2 = -self.rect_img.height

    def update(self):
        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed
        if self.bg_y1 >= self.rect_img.width:
            self.bg_y1 = -self.rect_img.width
        if self.bg_y2 >= self.rect_img.width:
            self.bg_y2 = -self.rect_img.width
        self.screen.blit(self.bg_img, (self.bg_y1, 0))
        self.screen.blit(self.bg_img, (self.bg_y2, 0))