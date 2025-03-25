from Classes.Passaro import Passaro
from Classes.Cano import Cano
from Classes.CanoSuperior import Cano_superior
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

clock = pygame.time.Clock()
pygame.init()
largura, altura = 800, 600
pygame.display.set_mode((largura, altura), DOUBLEBUF | OPENGL)
gluOrtho2D(0, largura, 0, altura)

# Definir o espaçamento mínimo entre os canos superior e inferior
espaco_entre_canos = 300

# Criação dos objetos
passaro = Passaro()
canos = [
    Cano(800, 150), Cano(1000, 175), Cano(1200, 100), Cano(1400, 100),
    Cano(1600, 150), Cano(1800, 250), Cano(2000, 100), Cano(2200, 50)
]

# Ajuste dos canos superiores para garantir o espaçamento adequado
canosup = [
    Cano_superior(900, 500), Cano_superior(1300, 550), Cano_superior(1200, 400),
    Cano_superior(1400, 450), Cano_superior(1600, 400), Cano_superior(1800, 450),
    Cano_superior(2000, 500), Cano_superior(2200, 500)
]

# Ajustar a altura dos canos superiores de acordo com a altura dos canos inferiores
for i in range(len(canos)):
    canosup[i].altura = canos[i].altura + espaco_entre_canos  # Definir altura para cano superior

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False

    # Verificar se a tecla espaço está pressionada durante toda a execução
    keys = pygame.key.get_pressed()
    if keys[K_SPACE]:
        passaro.pular()  # O pássaro vai pular enquanto a tecla for pressionada

    # Atualiza o estado do pássaro e os canos a cada quadro
    passaro.atualizar()
    glClear(GL_COLOR_BUFFER_BIT)

    # Desenhar o pássaro
    passaro.desenhar()

    # Atualizar e desenhar os canos
    for cano in canos:
        cano.atualizar()
        cano.desenhar()

    # Atualizar e desenhar os canos superiores
    for cano_superior in canosup:
        cano_superior.atualizar()
        cano_superior.desenhar()

    pygame.display.flip()  # Atualiza a tela para o novo quadro

    clock.tick(60)  # Limita a execução a 60 quadros por segundo

pygame.quit()
