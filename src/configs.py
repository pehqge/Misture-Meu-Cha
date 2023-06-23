import pygame
from src.assets import bg

# Informacao do Jogo
pygame.init()
WIDTH = 360
HEIGHT = 640
FPS = 60
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN.fill("#FFD8D7")
pygame.display.set_caption("misture meu chá!")
pygame.display.set_icon(pygame.image.load("assets/icone.png"))

# Inicializacao de variaveis
global state_menu, state_creditos, state_gameplay, state_gameover
state_menu = 0
state_creditos = 1
state_gameplay = 2
state_gameover = 3
scroll = -83
timer = None
game_state = state_menu
pausado = False
highs = False
cor_mortos = 0
contador = 0
FramePerSec = pygame.time.Clock()


# incializacao do background
def background():
    global scroll
    scroll += .5
    if scroll > 0:
        scroll = -83
    SCREEN.blit(bg, (0, scroll))