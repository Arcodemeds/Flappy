import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Cano:
    def __init__(self, x, altura):
        self.x = x
        self.largura = 50
        self.altura = altura
        self.espaco = 150  # Espaço entre o cano inferior e o superior
        self.velocidade = 3

    def atualizar(self):
        self.x -= self.velocidade  # Apenas move para a esquerda

    def desenhar(self):
        glColor3f(0, 1, 0)
        glBegin(GL_QUADS)
        glVertex2f(self.x, 0)
        glVertex2f(self.x + self.largura, 0)
        glVertex2f(self.x + self.largura, self.altura)
        glVertex2f(self.x, self.altura)
        glEnd()
