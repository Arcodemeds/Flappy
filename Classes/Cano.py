from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Cano:
    def __init__(self, x, altura):
        self.x = x
        self.largura = 50
        self.altura = altura
        self.velocidade = 3
        self.pontuado = False

    def atualizar(self, velocidade):
        self.x -= velocidade

    def desenhar(self):
        glBegin(GL_QUADS)
        # Lado esquerdo - sombra
        glColor3f(0.0, 0.3, 0.0)
        glVertex2f(self.x, 0)
        glVertex2f(self.x + self.largura * 0.2, 0)
        glVertex2f(self.x + self.largura * 0.2, self.altura)
        glVertex2f(self.x, self.altura)
        # Centro - cor principal
        glColor3f(0.0, 0.6, 0.0)
        glVertex2f(self.x + self.largura * 0.2, 0)
        glVertex2f(self.x + self.largura * 0.8, 0)
        glVertex2f(self.x + self.largura * 0.8, self.altura)
        glVertex2f(self.x + self.largura * 0.2, self.altura)
        # Lado direito - destaque
        glColor3f(0.0, 0.9, 0.0)
        glVertex2f(self.x + self.largura * 0.8, 0)
        glVertex2f(self.x + self.largura, 0)
        glVertex2f(self.x + self.largura, self.altura)
        glVertex2f(self.x + self.largura * 0.8, self.altura)
        glEnd()
