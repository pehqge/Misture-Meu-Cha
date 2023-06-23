from pygame import Rect, mouse, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from src.assets import iniciar, iniciar_f, bcreditos, bcreditos_f, voltar, voltar_f, sair, sair_f, b_menu, b_menu_f, denovo, denovo_f
global state_gameover, state_creditos, state_menu, state_gameplay, game_state
from src.configs import SCREEN, state_gameplay, state_creditos, state_menu, game_state
from src.tools import meio
from src.entities.xicara import xicara_gameplay


class Botao:
    def __init__(self, nome, nome_f, x, y, estado, fx=10, fy=7):
        self.nome = nome
        self.nome_f = nome_f
        self.x = x
        self.y = y
        self.fx = fx
        self.fy = fy
        self.estado = estado
        self.pressed = False

    def draw(self):
        rect = Rect(self.x, self.y, self.nome.get_width(), self.nome.get_height())
        if rect.collidepoint(mouse.get_pos()):
            pos_texto = (self.x + self.fx/3, self.y + self.fy/7)
            if self.pressed:
                pos_texto = (self.x + self.fx, self.y + self.fy)
        else:
            self.pressed = False
            pos_texto = (self.x, self.y)

        SCREEN.blit(self.nome_f, (self.x + self.fx, self.y + self.fy))
        SCREEN.blit(self.nome, pos_texto)
    
    def handle_event(self, event, Bool=False):
        rect = Rect(self.x, self.y, self.nome.get_width(), self.nome.get_height())
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if rect.collidepoint(mouse.get_pos()):
                    self.pressed = True
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                if rect.collidepoint(mouse.get_pos()):
                    if self.pressed:
                        if Bool:
                            global cor_mortos, timer, highs, lista_setas
                            cor_mortos = 0
                            xicara_gameplay.update_face(0)
                            xicara_gameplay.angulo = 0
                            timer = None
                            highs = False
                            xicara_gameplay.cx = 119
                            xicara_gameplay.cy = 300
                            lista_setas = []
                        game_state = self.estado
                    self.pressed = False

# definindo botoes
b_iniciar = Botao(iniciar, iniciar_f, 97, 457, state_gameplay)
b_creditos = Botao(bcreditos, bcreditos_f, 77, 540, state_creditos)
b_voltar = Botao(voltar, voltar_f, meio(voltar), 400, state_menu)
b_sair = Botao(sair, sair_f, 314, 11, state_menu, 6, 4)
b_menu = Botao(b_menu, b_menu_f, 196.79, 564, state_menu)
b_denovo = Botao(denovo, denovo_f, 185, 501, state_gameplay)