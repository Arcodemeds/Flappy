import random
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Classes.Passaro import Passaro
from Classes.Cano import Cano
from Classes.CanoSuperior import Cano_superior

# Inicializa o GLUT (necessário para desenhar texto)
glutInit()

clock = pygame.time.Clock()
pygame.init()
largura, altura = 800, 600
pygame.display.set_mode((largura, altura), DOUBLEBUF | OPENGL)
gluOrtho2D(0, largura, 0, altura)

# Função para desenhar texto usando GLUT
def draw_text(x, y, text):
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

# Gap fixo entre o cano inferior e o superior (usado para calcular a altura do cano superior)
espaco_entre_canos = 150  # ajuste conforme necessário

# Parâmetros para reposicionamento (gap entre canos na horizontal)
gap_min = 150
gap_max = 300

# Criação dos objetos iniciais
passaro = Passaro()
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

score = 0
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
        # Atualiza os objetos
        passaro.atualizar()

        # Verifica se o pássaro tocou o chão ou o teto:
        if (passaro.y - 15) <= 0 or (passaro.y + 15) >= altura:
            game_over = True

        for cano in canos:
            cano.atualizar()
        for cano_superior in canosup:
            cano_superior.atualizar()

        # Atualiza pontuação: se o cano passou do pássaro e não foi pontuado ainda
        for cano in canos:
            if not cano.pontuado and (cano.x + cano.largura) < passaro.x:
                score += 1
                cano.pontuado = True

        # Reposiciona os canos que saíram da tela (evita sobreposição)
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

        # Verifica colisões com os canos
        for cano in canos:
            if passaro.colidiu_inferior(cano):
                game_over = True
        for cano_superior in canosup:
            if passaro.colidiu_superior(cano_superior):
                game_over = True

    # Desenha a cena
    glClear(GL_COLOR_BUFFER_BIT)
    passaro.desenhar()
    for cano in canos:
        cano.desenhar()
    for cano_superior in canosup:
        cano_superior.desenhar()

    # Desenha o placar
    glColor3f(1, 1, 1)
    draw_text(10, 580, "Score: " + str(score))
    if game_over:
        draw_text(300, 300, "GAME OVER! Pressione ENTER para sair.")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
