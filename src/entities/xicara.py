from src.assets import xic_tras, colher, xic_frente, cara_main, cara_1, cara_2, cara_over, xic_tras_morta
from src.configs import SCREEN
from pygame import transform


class Xicara:
    def __init__(self, x, y, cara, Bool=True):
        self.x = x
        self.y = y
        self.xic_tras = xic_tras
        self.colher = colher
        self.xic_frente = xic_frente
        self.cara = cara
        self.Bool = Bool
        self.angulo = 0
        self.cx = x+98
        self.cy = y-38
        self.velocidade = 2

    def draw(self):
        SCREEN.blit(self.xic_tras, (self.x, self.y))
        if self.Bool:
            colher_rotacionada = transform.rotate(self.colher, self.angulo)
            SCREEN.blit(colher_rotacionada, (self.cx, self.cy))
        SCREEN.blit(self.xic_frente, (self.x, self.y))
        SCREEN.blit(self.cara, (self.x+67, self.y+54))
        # rotacao da colher

    def update_face(self, i):
        self.i = i
        if self.i == 0:
            self.cara = cara_main
            self.xic_tras = xic_tras
        elif self.i == 1:
            self.cara = cara_1
        elif self.i == 2:
            self.cara = cara_2
        elif self.i == 3:
            self.cara = cara_over
            self.xic_tras = xic_tras_morta
        
xicara_gameplay = Xicara(21, 338, cara_main)
