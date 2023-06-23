import pygame
from src.configs import *
from src.tools import *
from src.entities.seta import lista_setas
from src.game.gameplay import gameplay
from src.entities.botao import b_iniciar, b_creditos, b_voltar, b_denovo, b_sair, b_menu
from src.game.menu import menu
from src.game.creditos import creditos
from src.game.gameover import gameover
    
  
    

def main():
    global game_state

    while True:
        keys = {} 
        # logica menu principal
        while game_state == state_menu:
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
        while game_state == state_creditos:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                    b_voltar.handle_event(event)
            update_game_display()
            creditos()
                
        while game_state == state_gameplay:
            global lista_setas
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                    b_sair.handle_event(event, True)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        for seta in [x for x in lista_setas if x.tipo == 1]:
                            if seta.clique():
                                seta.win()
                    # if event.type =
                    
            update_game_display()
            gameplay()
            
        while game_state == state_gameover:
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
    