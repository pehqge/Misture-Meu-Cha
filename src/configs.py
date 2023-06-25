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
FramePerSec = pygame.time.Clock()

    
# Inicializacao de variaveis

class Var:
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
    score = ''
    score_max = ''
    tempo = 1
    idx = 0
    playing_music = False
    playing_gameplay_music = False
    playing_high = False
    playing_dead = False


# incializacao do background
def background():
    Var.scroll += .5
    if Var.scroll > 0:
        Var.scroll = -83
    SCREEN.blit(bg, (0, Var.scroll))