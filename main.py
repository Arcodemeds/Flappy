import random
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Classes.Passaro import Passaro
from Classes.Cano import Cano
from Classes.CanoSuperior import Cano_superior
from Classes.Fundo import desenhar_fundo, fundo_largura
import Classes.Fundo as Fundo

glutInit()
clock = pygame.time.Clock()
pygame.init()
largura, altura = 800, 600
pygame.display.set_mode((largura, altura), DOUBLEBUF | OPENGL)

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

Fundo.carregar_textura_fundo("Assets/Fundo.jpeg")
gluOrtho2D(0, largura, 0, altura)

def draw_text(x, y, text):
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

espaco_entre_canos = 150
gap_min = 150
gap_max = 300

passaro = Passaro()
canos = [Cano(800, 150), Cano(1000, 175), Cano(1200, 100), Cano(1400, 100),
         Cano(1600, 150), Cano(1800, 250), Cano(2000, 100), Cano(2200, 50)]
canosup = [Cano_superior(cano.x, cano.altura + espaco_entre_canos) for cano in canos]

score = 0
velocidade_jogo = 2
pos_fundo = 0
game_over = False
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False
        if evento.type == KEYDOWN:
            if evento.key == K_SPACE and not game_over:
                passaro.pular()
            if evento.key == K_RETURN and game_over:
                rodando = False

    if not game_over:
        passaro.atualizar()
        if (passaro.y - 15) <= 0 or (passaro.y + 15) >= altura:
            game_over = True

        for cano, cano_sup in zip(canos, canosup):
            cano.atualizar(velocidade_jogo)
            cano_sup.atualizar(velocidade_jogo)

        for cano in canos:
            if not cano.pontuado and (cano.x + cano.largura) < passaro.x:
                score += 1
                if score % 5 == 0:
                    velocidade_jogo += 0.5
                cano.pontuado = True

        max_x = max(c.x for c in canos)
        for i in range(len(canos)):
            if canos[i].x < -canos[i].largura:
                novo_gap = random.randint(gap_min, gap_max)
                novo_x = max_x + novo_gap
                nova_altura = random.randint(100, 250)
                canos[i].x = novo_x
                canos[i].altura = nova_altura
                canos[i].pontuado = False
                canosup[i].x = novo_x
                canosup[i].altura = nova_altura + espaco_entre_canos
                max_x = novo_x

        for cano in canos:
            if passaro.colidiu_inferior(cano):
                game_over = True
        for cano_superior in canosup:
            if passaro.colidiu_superior(cano_superior):
                game_over = True

    if not game_over:
        pos_fundo -= velocidade_jogo

    glClear(GL_COLOR_BUFFER_BIT)
    desenhar_fundo(pos_fundo, altura)
    passaro.desenhar()
    for cano in canos:
        cano.desenhar()
    for cano_superior in canosup:
        cano_superior.desenhar()

    glColor3f(1, 1, 1)
    draw_text(10, 580, f"Score: {score}")

    if game_over:
        draw_text(300, 300, "GAME OVER! Pressione ENTER para sair.")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
