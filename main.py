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

# Espaçamento entre os canos (usado para ajustar o cano superior)
espaco_entre_canos = 300

# Criação dos objetos
passaro = Passaro()
canos = [
    Cano(800, 150), Cano(1000, 175), Cano(1200, 100), Cano(1400, 100),
    Cano(1600, 150), Cano(1800, 250), Cano(2000, 100), Cano(2200, 50)
]

canosup = [
    Cano_superior(900, 500), Cano_superior(1300, 550), Cano_superior(1200, 400),
    Cano_superior(1400, 450), Cano_superior(1600, 400), Cano_superior(1800, 450),
    Cano_superior(2000, 500), Cano_superior(2200, 500)
]

# Ajusta a altura dos canos superiores para que o gap seja o desejado.
# Para cada cano inferior, o cano superior deve iniciar em: (altura_inferior + espaco_entre_canos)
for i in range(len(canos)):
    canosup[i].altura = canos[i].altura + espaco_entre_canos

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False

    keys = pygame.key.get_pressed()
    if keys[K_SPACE]:
        passaro.pular()

    # Atualiza os objetos
    passaro.atualizar()
    for cano in canos:
        cano.atualizar()
    for cano_superior in canosup:
        cano_superior.atualizar()

    # Verifica colisão com os canos inferiores
    for cano in canos:
        if passaro.colidiu_inferior(cano):
            print("Colisão com cano inferior!")
            rodando = False

    # Verifica colisão com os canos superiores
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
