class Settings:
    """class to store the game settings"""

    def __init__(self):
        """Initialise settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (192, 192, 192)
        self.ship_speed = 3.0
        self.ship_limit = 3
        # bullets
        self.bullet_speed = 4.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
        # aliens
        self.alien_speed = 3.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
