class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_colour = (255, 255, 255)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
        self.bullet_allow = 3

        # Alien settings
        self.alien_speed = 1
        self.fleet_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
