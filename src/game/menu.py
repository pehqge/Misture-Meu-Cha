from src.configs import background, WIDTH, SCREEN
from src.assets import fonte_scoremax, logo, mesa, cara_main
from src.tools import score_max, seno, update_game_display
from src.entities.xicara import Xicara
from src.entities.botao import b_iniciar, b_creditos



def menu():
    
    background()
    # high score
    best_score = fonte_scoremax.render("best score   " + str(score_max), True, "#F38489")
    best_score_rect = best_score.get_rect(center=(WIDTH//2, 40))
    SCREEN.blit(best_score, best_score_rect)
    
    # logo mexendo
    y = seno(200.0, 1280, 6.0, 60)
    SCREEN.blit(logo, (-17, y))
    
    SCREEN.blit(mesa, (0, 358))
    
    # xicara do menu
    xicara_menu = Xicara(58, 281, cara_main)
    xicara_menu.draw()
    
    # botoes
    b_iniciar.draw()
    b_creditos.draw()
    
    # FPS
    update_game_display()