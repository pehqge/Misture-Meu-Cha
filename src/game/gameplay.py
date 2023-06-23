from src.configs import SCREEN, WIDTH, state_gameover, background, state_gameplay
from src.assets import coracao, coracao_dead, mesa, setav_d, setav_l, setav_u, setav_r, timerbox, fonte_score
from src.tools import update_game_display, meio
from pygame import key, time, K_LEFT, K_RIGHT, K_UP, K_DOWN
from src.entities.seta import Seta, lista_setas
from src.entities.botao import b_sair

def gameplay():
    global game_state, timer, timer_str, lista_setas, contador, segundos, cor_mortos
    background()
    SCREEN.blit(mesa, (0, 418))
    
    # xicara do gameplay
    xicara_gameplay.draw()
    b_sair.draw()
    
    # coracoes
    draw_coracoes(cor_mortos)
        
    # setas
    keys = key.get_pressed()
    if keys[K_LEFT]:
        setav_l.set_alpha(255)
        xicara_gameplay.angulo = max(xicara_gameplay.angulo - 4, 0)
        xicara_gameplay.cx = max(xicara_gameplay.cx - 4, 70)
    else:
        setav_l.set_alpha(168)
    if keys[K_RIGHT]:
        xicara_gameplay.angulo = min(xicara_gameplay.angulo + 4, 65)
        xicara_gameplay.cx = min(xicara_gameplay.cx + 4, 110)
        setav_r.set_alpha(255)
    else:
        setav_r.set_alpha(168)
    if keys[K_UP]:
        xicara_gameplay.cy = max(xicara_gameplay.cy - 2, 260)
        setav_u.set_alpha(255)
    else:
        setav_u.set_alpha(168)
    if keys[K_DOWN]:
        xicara_gameplay.cy = min(xicara_gameplay.cy + 2, 300)
        setav_d.set_alpha(255)
    else:
        setav_d.set_alpha(168)

    # Desenha as setas na tela
    SCREEN.blit(setav_l, (30.5, 180))
    SCREEN.blit(setav_r, (258, 180))
    SCREEN.blit(setav_u, (120, 170))
    SCREEN.blit(setav_d, (188, 170))
    
    # score
    if game_state == state_gameplay and timer is None:
        timer = time.get_ticks()
    SCREEN.blit(timerbox, (meio(timerbox), 513))
    if timer is not None:
        tempo_passado = time.get_ticks() - timer
        minutos = int(tempo_passado / 60000)
        segundos = int((tempo_passado % 60000) / 1000)
        timer_str = f"{minutos}:{segundos:02d}"
        timer_text = fonte_score.render(timer_str, True, "#454653")
        timer_rect = timer_text.get_rect(center=(WIDTH//2, 575))
        SCREEN.blit(timer_text, timer_rect)

    if segundos >= 1:
        contador += 1
        if contador == 30:
            lista_setas.append(Seta())
            contador = 0
        
    
    for seta in lista_setas:
        if seta.y > 220:
            seta.lose()
            if seta.lose():
                continue
            
            if seta.opacidade < 0:
                lista_setas.remove(seta)
                mata()
                continue
        seta.move()
        seta.draw()
    
    update_game_display()


def draw_coracoes(num_mortos):
    for i in range(3):
        if i < 3 - num_mortos:
            SCREEN.blit(coracao, (245 + 35 * i, 314))
        else:
            SCREEN.blit(coracao_dead, (245 + 35 * i, 314))

def mata():
    global cor_mortos, xicara_gameplay, game_state, score
    cor_mortos += 1
    xicara_gameplay.update_face(cor_mortos)
    if cor_mortos == 3:
        score = timer_str
        game_state = state_gameover