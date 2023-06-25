import pygame
from src.configs import *
from src.tools import *
from src.game.gameplay import gameplay
from src.entities.botao import b_iniciar, b_creditos, b_voltar, b_denovo, b_sair, b_menu
from src.entities.seta import Seta
from src.game.menu import menu
from src.game.creditos import creditos
from src.game.gameover import gameover
    
def update_game_display():
    pygame.display.update()
    FramePerSec.tick(FPS)
    
def lista_conf(tipo):    
    return [x for x in Seta.lista_setas if x != None and x.tipo == tipo]
def main():

    while True:
        
        # if Var.game_state == Var.state_creditos or Var.game_state == Var.state_menu:
        #     pygame.mixer.music.load("assets/menu.wav")
        #     pygame.mixer.music.play(-1)
            
        # logica menu principal
        while Var.game_state == Var.state_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                    b_iniciar.handle_event(event)
                    b_creditos.handle_event(event)
            update_game_display()
            menu()
            
        # logica creditos
        while Var.game_state == Var.state_creditos:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                    b_voltar.handle_event(event)
            update_game_display()
            creditos()
                
        while Var.game_state == Var.state_gameplay:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                    b_sair.handle_event(event, True)
                elif event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_UP, pygame.K_w]:
                        for seta in lista_conf(1):
                            if seta.clique():
                                seta.verificador = True
                    if event.key in [pygame.K_LEFT, pygame.K_a]:
                        for seta in lista_conf(0):
                            if seta.clique():
                                seta.verificador = True
                    if event.key in [pygame.K_DOWN, pygame.K_s]:
                        for seta in lista_conf(2):
                            if seta.clique():
                                seta.verificador = True
                    if event.key in [pygame.K_RIGHT, pygame.K_d]:
                        for seta in lista_conf(3):
                            if seta.clique():
                                seta.verificador = True
                    
            gameplay()
            update_game_display()
            
        while Var.game_state == Var.state_gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                    b_menu.handle_event(event, True)
                    b_denovo.handle_event(event, True)
            update_game_display()
            gameover()
                
            
if __name__ == "__main__":
    main()
    