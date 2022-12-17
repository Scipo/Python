import pygame
from setting import Settings
from ship import Ship
from alien import Alien
from game_stat import GameStat
import game_function as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Create an instance to store game statistics.
    stat = GameStat(ai_settings)
    # Make ship
    ship = Ship(ai_settings, screen)
    # Make alien
    alien = Alien(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    # Maje a group of aliens
    alien = Group()
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, alien)
    # Starting main loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, alien, bullets)
        gf.update_aliens(ai_settings, stat, screen, ship, alien, bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)


run_game()
