from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Cano_superior:
    def __init__(self, x, altura):
        self.x = x
        self.largura = 50
        self.altura = altura  # Essa altura será ajustada para (altura do inferior + espaço)
        self.espaco = 150
        self.velocidade = 3

    def atualizar(self):
        self.x -= self.velocidade
        if self.x < self.velocidade:
            self.x = 800

    def desenhar(self):
        glColor3f(0, 1, 0)
        glBegin(GL_QUADS)
        glVertex2f(self.x, 600)
        glVertex2f(self.x + self.largura, 600)
        glVertex2f(self.x + self.largura, self.altura)
        glVertex2f(self.x, self.altura)
        glEnd()
