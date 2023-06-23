import random
from src.assets import acerto, seta_l, seta_u, seta_d, seta_r, missed
from pygame import time
from src.configs import SCREEN


lista_setas = []

class Seta:
    global lista_setas
    def __init__(self):
        self.velocidade = random.randint(2, 8) #TESTANDO
        self.opacidade = 255
        self.y = -60 #TESTAR
        self.ye = 183
        self.last_tipo = None
        self.tipo = self.gerar_tipo()
        if self.tipo == 0: #esquerda
            self.x = 30.5
            self.xe = 48
            self.ya = 155
            self.xa = 51
            self.img = seta_l
        elif self.tipo == 1: #cima
            self.x = 120
            self.xe = 122
            self.ya = 188
            self.xa = 134
            self.img = seta_u
        elif self.tipo == 2: #baixo
            self.x = 188
            self.xe = 192
            self.ya = 188
            self.xa = 203
            self.img = seta_d
        elif self.tipo == 3: #direita
            self.x = 258
            self.xe = 264
            self.ya = 155
            self.xa = 300
            self.img = seta_r
        self.error = missed
        self.contador = True
        
    def move(self):
        self.y += self.velocidade
        
    def draw(self):
        SCREEN.blit(self.img, (self.x, self.y))
        
    def lose(self):
        self.opacidade -= 40
        self.img.set_alpha(self.opacidade)
        if self.contador:
                self.contador = False
                self.error_start_time = time.get_ticks()
        self.current_time = time.get_ticks()
        if self.current_time - self.error_start_time <= 1000:
                SCREEN.blit(self.error, (self.xe, self.ye))
                
    def win(self):
        global lista_setas
        if self.contador:
                self.contador = False
                self.win_start_time = time.get_ticks()
        self.current_time = time.get_ticks()
        if self.current_time - self.win_start_time <= 1000:
                SCREEN.blit(acerto, (self.xa, self.ya))
        else:
            lista_setas.remove(self)
                
    def gerar_tipo(self):
        tipo = random.randint(0, 3)
        if len(lista_setas) > 0:
            last_tipo = lista_setas[-1].tipo
            while tipo == last_tipo:
                tipo = random.randint(0, 3)
        return tipo
    
    def clique(self):
        if self.tipo in [0, 3]:
            if self.y >= 170 and self.y <= 190:
                return True
        elif self.tipo in [1, 2]:
            if self.y >= 160 and self.y <= 180:
                return True
        return False
            
