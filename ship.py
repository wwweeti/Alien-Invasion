import pygame

class Ship:
    def __init__(self,ai_game):

        self.ikkuna_ship=ai_game.ikkuna
        self.kuva=pygame.image.load("images/ship.bmp")
        self.kuva_kehys=self.kuva.get_rect()
        self.ikkuna_kehys=ai_game.ikkuna.get_rect()
        self.kuva_kehys.midbottom=self.ikkuna_kehys.midbottom

    def blitme(self):
        self.ikkuna_ship.blit(self.kuva,self.kuva_kehys)