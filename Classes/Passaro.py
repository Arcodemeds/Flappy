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

    def colidiu_inferior(self, cano):
        bird_left   = self.x - 15
        bird_right  = self.x + 15
        bird_bottom = self.y - 15
        bird_top    = self.y + 15

        pipe_left   = cano.x
        pipe_right  = cano.x + cano.largura
        pipe_bottom = 0
        pipe_top    = cano.altura

        if bird_right < pipe_left or bird_left > pipe_right or bird_top < pipe_bottom or bird_bottom > pipe_top:
            return False
        return True

    def colidiu_superior(self, cano):
        bird_left   = self.x - 15
        bird_right  = self.x + 15
        bird_bottom = self.y - 15
        bird_top    = self.y + 15

        pipe_left   = cano.x
        pipe_right  = cano.x + cano.largura
        pipe_bottom = cano.altura
        pipe_top    = 600

        if bird_right < pipe_left or bird_left > pipe_right or bird_top < pipe_bottom or bird_bottom > pipe_top:
            return False
        return True
