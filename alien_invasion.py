import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.ikkuna = pygame.display.set_mode((self.settings.leveys, self.settings.korkeus))
        self.ship = Ship(self)
        pygame.display.set_caption("Alien invasion")

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.ship.liikkuu_vasemmalle=True
                elif event.key==pygame.K_d:
                    self.ship.liikkuu_oikealle=True

            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_a:
                    self.ship.liikkuu_vasemmalle=False
                elif event.key==pygame.K_d:
                    self.ship.liikkuu_oikealle=False

    def _update_screen(self):
        self.ikkuna.fill(self.settings.tauluväri)
        self.ship.blitme()
        pygame.display.flip()


ai = AlienInvasion()
ai.run_game()
