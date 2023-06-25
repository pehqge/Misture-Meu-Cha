from src.configs import SCREEN, WIDTH, Var, background
from src.assets import coracao, coracao_dead, mesa, setav_d, setav_l, setav_u, setav_r, timerbox, fonte_score, mini_high, fonte_mini_high
from src.tools import meio
from pygame import key, time, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_a, K_s, K_d, K_w, mixer
from src.entities.seta import Seta
from src.entities.botao import b_sair
from src.entities.xicara import xicara_gameplay

def gameplay():
    if Var.playing_music or Var.playing_dead or Var.playing_high:
        mixer.music.fadeout(200)
        mixer.music.set_volume(0.3)
        Var.playing_music = False
        Var.playing_dead = False
        Var.playing_high = False
        
    if not Var.playing_gameplay_music:
        mixer.music.load("assets/gameplay.wav")
        mixer.music.play(-1)
        mixer.music.set_volume(0.2)
        Var.playing_gameplay_music = True
        
        
    Var.tempo += 0.0003
    if Var.tempo >= 2:
        Var.tempo = 2
    background()
    SCREEN.blit(mesa, (0, 418))
    
    # xicara do gameplay
    xicara_gameplay.draw()
    b_sair.draw()
    
    # coracoes
    draw_coracoes(Var.cor_mortos)
        
    # setas
    keys = key.get_pressed()
    if keys[K_LEFT] or keys[K_a]:
        setav_l.set_alpha(255)
        xicara_gameplay.angulo = max(xicara_gameplay.angulo - 4, 0)
        xicara_gameplay.cx = max(xicara_gameplay.cx - 4, 70)
    else:
        setav_l.set_alpha(168)
    if keys[K_RIGHT] or keys[K_d]:
        xicara_gameplay.angulo = min(xicara_gameplay.angulo + 4, 65)
        xicara_gameplay.cx = min(xicara_gameplay.cx + 4, 110)
        setav_r.set_alpha(255)
    else:
        setav_r.set_alpha(168)
    if keys[K_UP] or keys[K_w]:
        xicara_gameplay.cy = max(xicara_gameplay.cy - 2, 260)
        setav_u.set_alpha(255)
    else:
        setav_u.set_alpha(168)
    if keys[K_DOWN] or keys[K_s]:
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
    if Var.game_state == Var.state_gameplay and Var.timer is None:
        Var.timer = time.get_ticks()
    SCREEN.blit(timerbox, (meio(timerbox), 513))
    SCREEN.blit(mini_high, (233, 500))
    global timer_str, segundos
    if Var.timer is not None:
        tempo_passado = time.get_ticks() - Var.timer
        minutos = int(tempo_passado / 60000)
        segundos = int((tempo_passado % 60000) / 1000)
        timer_str = f"{minutos}:{segundos:02d}"
        timer_text = fonte_score.render(timer_str, True, "#454653")
        timer_rect = timer_text.get_rect(center=(WIDTH//2, 575))
        SCREEN.blit(timer_text, timer_rect)
        ministr = f"best {Var.score_max}"
        if Var.score_max < timer_str:
            ministr = "HIGH SCORE"
        minihigh_text = fonte_mini_high.render(ministr, True, "#fefefe")
        minihigh_rect = minihigh_text.get_rect(center=(288.8, 518))
        SCREEN.blit(minihigh_text, minihigh_rect)

    if segundos >= 1:
        Var.contador += 1
        if Var.contador >= 55//Var.tempo:
            Seta.lista_setas[Var.idx] = Seta(Var.idx)
            Var.idx += 1
            if Var.idx == 8:
                Var.idx = 0
            Var.contador = 0
        
    
    for seta in [x for x in Seta.lista_setas if x != None]:
        seta.y += seta.velocidade
        seta.draw()
        if seta.verificador:
            seta.win()
        if seta.y > 220:
            seta.lose()
            mata()            
    
def draw_coracoes(num_mortos):
    for i in range(3):
        if i < 3 - num_mortos:
            SCREEN.blit(coracao, (245 + 35 * i, 314))
        else:
            SCREEN.blit(coracao_dead, (245 + 35 * i, 314))

def mata():
    global timer_str
    if Var.cor_mortos == 3:
        Var.score = timer_str
        Var.idx = 0
        Var.contador = 0
        Var.game_state = Var.state_gameover