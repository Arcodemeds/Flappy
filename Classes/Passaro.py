from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Passaro:
    def __init__(self):
        self.x = 200
        self.y = 300
        self.velocidade = 0
        self.gravidade = -0.5

    def atualizar(self):
        self.velocidade += self.gravidade
        self.y += self.velocidade
        if self.y < 0:
            self.y = 0
            self.velocidade = 0

    def pular(self):
        self.velocidade = 6

    def desenhar(self):
        glColor3f(1, 1, 0)
        glBegin(GL_QUADS)
        glVertex2f(self.x - 15, self.y - 15)
        glVertex2f(self.x + 15, self.y - 15)
        glVertex2f(self.x + 15, self.y + 15)
        glVertex2f(self.x - 15, self.y + 15)
        glEnd()

    # Verificação de colisão com o cano inferior
    def colidiu_inferior(self, cano):
        # Retângulo do pássaro
        bird_left   = self.x - 15
        bird_right  = self.x + 15
        bird_bottom = self.y - 15
        bird_top    = self.y + 15

        # Retângulo do cano inferior
        pipe_left   = cano.x
        pipe_right  = cano.x + cano.largura
        pipe_bottom = 0
        pipe_top    = cano.altura

        # Se não houver interseção, não colidiu
        if bird_right < pipe_left or bird_left > pipe_right or bird_top < pipe_bottom or bird_bottom > pipe_top:
            return False
        return True

    # Verificação de colisão com o cano superior
    def colidiu_superior(self, cano):
        # Retângulo do pássaro
        bird_left   = self.x - 15
        bird_right  = self.x + 15
        bird_bottom = self.y - 15
        bird_top    = self.y + 15

        # Retângulo do cano superior
        pipe_left   = cano.x
        pipe_right  = cano.x + cano.largura
        # Aqui, a altura do cano superior foi ajustada para (altura inferior + espaço)
        pipe_bottom = cano.altura
        pipe_top    = 600  # Altura da janela

        if bird_right < pipe_left or bird_left > pipe_right or bird_top < pipe_bottom or bird_bottom > pipe_top:
            return False
        return True
