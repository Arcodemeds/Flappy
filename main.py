from Classes.Passaro import Passaro
from Classes.Cano import Cano
from Classes.CanoSuperior import Cano_superior
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

clock = pygame.time.Clock()
pygame.init()
largura, altura = 800, 600
pygame.display.set_mode((largura, altura), DOUBLEBUF | OPENGL)
gluOrtho2D(0, largura, 0, altura)

# Gap fixo entre o cano inferior e o superior (usado para calcular a altura do cano superior)
espaco_entre_canos = 150  # ajuste conforme necessário

# Parâmetros para reposicionamento (gap entre canos na horizontal)
gap_min = 150
gap_max = 300

# Criação dos objetos iniciais
passaro = Passaro()
# Inicialmente, os canos são criados em sequência com posições pré-definidas
canos = [
    Cano(800, 150), Cano(1000, 175), Cano(1200, 100), Cano(1400, 100),
    Cano(1600, 150), Cano(1800, 250), Cano(2000, 100), Cano(2200, 50)
]
canosup = [
    Cano_superior(800, 150 + espaco_entre_canos), Cano_superior(1000, 175 + espaco_entre_canos),
    Cano_superior(1200, 100 + espaco_entre_canos), Cano_superior(1400, 100 + espaco_entre_canos),
    Cano_superior(1600, 150 + espaco_entre_canos), Cano_superior(1800, 250 + espaco_entre_canos),
    Cano_superior(2000, 100 + espaco_entre_canos), Cano_superior(2200, 50 + espaco_entre_canos)
]

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False

    keys = pygame.key.get_pressed()
    if keys[K_SPACE]:
        passaro.pular()

    # Atualiza os objetos (apenas movimenta)
    passaro.atualizar()
    for cano in canos:
        cano.atualizar()
    for cano_superior in canosup:
        cano_superior.atualizar()

    # Reposiciona os canos que saíram da tela (evita sobreposição)
    # Primeiro, encontra o maior x atual entre os canos (inferior ou superior, já que devem estar sincronizados)
    max_x = max(c.x for c in canos)
    for i in range(len(canos)):
        if canos[i].x < -canos[i].largura:
            novo_gap = random.randint(gap_min, gap_max)
            novo_x = max_x + novo_gap
            nova_altura = random.randint(100, 250)
            # Reposiciona o cano inferior
            canos[i].x = novo_x
            canos[i].altura = nova_altura
            # Reposiciona o cano superior com base no inferior e no gap fixo
            canosup[i].x = novo_x
            canosup[i].altura = nova_altura + espaco_entre_canos
            max_x = novo_x  # Atualiza o maior x para as próximas reposições

    # Verifica colisões
    for cano in canos:
        if passaro.colidiu_inferior(cano):
            print("Colisão com cano inferior!")
            rodando = False
    for cano_superior in canosup:
        if passaro.colidiu_superior(cano_superior):
            print("Colisão com cano superior!")
            rodando = False

    # Desenha a cena
    glClear(GL_COLOR_BUFFER_BIT)
    passaro.desenhar()
    for cano in canos:
        cano.desenhar()
    for cano_superior in canosup:
        cano_superior.desenhar()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
