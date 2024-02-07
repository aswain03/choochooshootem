import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Mangages the ship(user)"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load image and get rect
        self.image = pygame.image.load("./sprites/defender_joe.bmp")
        self.rect = self.image.get_rect()

        # starting pos
        self.rect.midbottom = self.screen_rect.midbottom

        # ship horizontal pos
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """updating ships pos"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """draw in ship at curr location"""
        self.screen.blit(self.image, self.rect)
