import pygame


class Ship:
    def __init__(self, ai_game):

        self.settings_ship = ai_game.settings
        self.kuva = pygame.image.load("images/ship.png")
        self.kuva_kehys = self.kuva.get_rect()

        self.ikkuna_ship = ai_game.ikkuna
        self.ikkuna_kehys = self.ikkuna_ship.get_rect()

        self.kuva_kehys.midbottom = self.ikkuna_kehys.midbottom

        self.liikkuu_vasemmalle = False
        self.liikkuu_oikealle = False
        self.x=float(self.kuva_kehys.x)

    def blitme(self):
        self.ikkuna_ship.blit(self.kuva, self.kuva_kehys)

    def update(self):
        if self.liikkuu_vasemmalle and self.kuva_kehys.left >= 0:
            self.x -= self.settings_ship.ship_speed
        if self.liikkuu_oikealle and self.kuva_kehys.right <= self.ikkuna_kehys.right:
            self.x += self.settings_ship.ship_speed
        self.kuva_kehys.x=self.x