from src.configs import background, SCREEN, WIDTH, cor_mortos
from src.assets import mesa, game_over, timerbox, fonte_score, highscore_star
from src.tools import meio, set_highscore
from src.entities.xicara import xicara_gameplay
from src.game.gameplay import draw_coracoes
from src.entities.botao import b_menu, b_denovo

def gameover():
    global score, score_max, highs
    background()
    SCREEN.blit(mesa, (0, 418))
    SCREEN.blit(game_over, (meio(game_over), 53))
    SCREEN.blit(timerbox, (meio(timerbox), 131))
    score_text = fonte_score.render(score, True, "#454653")
    score_rect = score_text.get_rect(center=(WIDTH//2, 195))
    SCREEN.blit(score_text, score_rect)
    if score > score_max:
        highs = True
        score_max = score
        set_highscore(score)
    if highs:
        SCREEN.blit(highscore_star, (191.86, 201.52))
    xicara_gameplay.draw()
    draw_coracoes(cor_mortos)
    b_menu.draw()
    b_denovo.draw()