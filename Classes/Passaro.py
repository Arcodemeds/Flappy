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

    def desenhar (self):
        glColor3f(1, 1, 0)
        glBegin (GL_QUADS)
        glVertex2f(self.x - 15, self.y - 15)
        glVertex2f(self.x + 15, self.y - 15)
        glVertex2f(self.x + 15, self.y - 15)
        glVertex2f(self.x - 15, self.y + 15)
        glEnd()
