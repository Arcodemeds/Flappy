from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image

class Passaro:
    def __init__(self):
        self.x = 200
        self.y = 300
        self.velocidade = 0
        self.gravidade = -0.5
        self.textura = self.carregar_textura("Assets/passaro.png")  # Caminho para sua imagem

    def carregar_textura(self, caminho):
        imagem = Image.open(caminho)
        imagem = imagem.transpose(Image.FLIP_TOP_BOTTOM)
        img_data = imagem.convert("RGBA").tobytes()
        largura, altura = imagem.size

        textura_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, textura_id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, largura, altura, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        return textura_id
    def atualizar(self):
        self.velocidade += self.gravidade
        self.y += self.velocidade

    def pular(self):
        self.velocidade = 6

    def desenhar(self):
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.textura)
        glColor3f(1, 1, 1)  # Cor branca para não alterar as cores da imagem

        tamanho = 20
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex2f(self.x - tamanho, self.y - tamanho)
        glTexCoord2f(1, 0); glVertex2f(self.x + tamanho, self.y - tamanho)
        glTexCoord2f(1, 1); glVertex2f(self.x + tamanho, self.y + tamanho)
        glTexCoord2f(0, 1); glVertex2f(self.x - tamanho, self.y + tamanho)
        glEnd()
        glDisable(GL_TEXTURE_2D)

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
