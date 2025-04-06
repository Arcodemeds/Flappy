import random
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Classes.Passaro import Passaro
from Classes.Cano import Cano
from Classes.CanoSuperior import CanoSuperior
from Classes.Fundo import desenhar_fundo, carregar_textura_fundo

def inicializar():
    global passaro, canos, canosup, score, velocidade_jogo, pos_fundo, game_over, som_morte

    espaco_entre_canos = 150
    passaro = Passaro()
    canos = [Cano(800, 150), Cano(1000, 175), Cano(1200, 100), Cano(1400, 100),
             Cano(1600, 150), Cano(1800, 250), Cano(2000, 100), Cano(2200, 50)]
    canosup = [CanoSuperior(cano.x, cano.altura + espaco_entre_canos) for cano in canos]

    score = 0
    velocidade_jogo = 2
    pos_fundo = 0
    game_over = False

    # Inicializa o mixer do Pygame e carrega o som de morte
    pygame.mixer.init()
    som_morte = pygame.mixer.Sound("Assets/sfx_die.mp3")

def main():
    global game_over, pos_fundo, score, velocidade_jogo

    glutInit()
    clock = pygame.time.Clock()
    pygame.init()
    largura, altura = 800, 600
    pygame.display.set_mode((largura, altura), DOUBLEBUF | OPENGL)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    carregar_textura_fundo("Assets/Fundo.jpeg")
    gluOrtho2D(0, largura, 0, altura)

    def draw_text(x, y, text):
        glWindowPos2f(x, y)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

    inicializar()
    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                rodando = False
            if evento.type == KEYDOWN:
                if evento.key == K_SPACE and not game_over:
                    passaro.pular()
                if evento.key == K_RETURN and game_over:
                    inicializar()

        if not game_over:
            passaro.atualizar()
            if (passaro.y - 15) <= 0 or (passaro.y + 15) >= altura:
                game_over = True
                som_morte.play()  # Reproduz o som de morte

            for cano, cano_sup in zip(canos, canosup):
                cano.atualizar(velocidade_jogo)
                cano_sup.atualizar(velocidade_jogo)

            for cano in canos:
                if not cano.pontuado and (cano.x + cano.largura) < passaro.x:
                    score += 1
                    passaro.som_ponto.play()  # Reproduz o som de pontuação
                    if score % 5 == 0:
                        velocidade_jogo += 0.5
                    cano.pontuado = True

            max_x = max(c.x for c in canos)
            for i in range(len(canos)):
                if canos[i].x < -canos[i].largura:
                    novo_gap = random.randint(150, 300)
                    novo_x = max_x + novo_gap
                    nova_altura = random.randint(100, 250)
                    canos[i].x = novo_x
                    canos[i].altura = nova_altura
                    canos[i].pontuado = False
                    canosup[i].x = novo_x
                    canosup[i].altura = nova_altura + 150
                    max_x = novo_x

            for cano in canos:
                if passaro.colidiu_inferior(cano):
                    game_over = True
                    som_morte.play()  # Reproduz o som de morte
            for cano_superior in canosup:
                if passaro.colidiu_superior(cano_superior):
                    game_over = True
                    som_morte.play()  # Reproduz o som de morte

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
            draw_text(300, 300, "GAME OVER! Pressione ENTER para reiniciar.")

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
