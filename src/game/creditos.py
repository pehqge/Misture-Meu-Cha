from src.configs import background, SCREEN
from src.assets import mesa, logo, pedro, cara_creditos
from src.tools import meio, update_game_display
from src.entities.xicara import Xicara
from src.entities.botao import b_voltar

def creditos():
    background()
    # bg
    SCREEN.blit(mesa, (0, 523))
    SCREEN.blit(logo, (-17, 0))
    SCREEN.blit(pedro, (meio(pedro), 200))

    # xicara dos creditos
    xicara_creditos = Xicara(61.5, 458, cara_creditos, False)
    xicara_creditos.draw()
    
    # botao de voltar
    b_voltar.draw()
    
    # FPS
    update_game_display()