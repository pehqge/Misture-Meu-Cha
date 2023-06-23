from json import load, dump
from pygame import time, display
from math import sin
from src.configs import WIDTH, FPS, FramePerSec

# funcoes do highscore
def get_highscore():
    with open("score.json", "r") as f:
        return load(f)["best"]
def set_highscore(score):
    with open("score.json", "w") as f:
        dump({"best": score}, f)
score_max = get_highscore()

# alinha a imagem para o meio
def meio(imagem):
    largura_imagem = imagem.get_width()
    posicao_x = (WIDTH - largura_imagem) // 2
    return posicao_x

# funcao seno para animacoes
def seno(vel, tempo, longe, Yinicial):
	t = time.get_ticks() / 2 % tempo
	x = t
	y = sin(t/vel) * longe + Yinicial 
	y = int(y)
	return y

# atualizacao de FPS
def update_game_display():
    display.update()
    FramePerSec.tick(FPS)