import pygame
from pygame.sprite import Sprite


# class Bullet(Sprite):
#     """manages the rounds fired (pygame sprite)"""

#     def __init__(self, ai_game):
#         super().__init__()
#         self.screen = ai_game.screen
#         self.settings = ai_game.settings
#         self.color = self.settings.bullet_color

#         self.rect = pygame.Rect(
#             0, 0, self.settings.bullet_width, self.settings.bullet_height
#         )
#         self.rect.midtop = ai_game.ship.rect.midtop

#         self.y = float(self.rect.y)

#     def update(self):
#         """move rounds"""
#         self.y -= self.settings.bullet_speed
#         self.rect.y = self.y

#     def draw_bullet(self):
#         pygame.draw.rect(self.screen, self.color, self.rect)


class Bullet(Sprite):
    """manages the rounds fired (custom sprite)"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load("./sprites/no.bmp")
        self.rect = self.image.get_rect()

        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """move rounds"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)
