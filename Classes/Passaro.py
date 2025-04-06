import pygame
from OpenGL.GL import *
from PIL import Image

class Passaro:
    def __init__(self):
        self.x = 200
        self.y = 300
        self.velocidade = 0
        self.gravidade = -0.5
        self.textura = self.carregar_textura("Assets/Passaro.png")

        # Inicializa o mixer do Pygame
        pygame.mixer.init()
        # Carrega os sons
        self.som_pulo = pygame.mixer.Sound("Assets/sfx_wing.mp3")
        self.som_ponto = pygame.mixer.Sound("Assets/sfx_point.mp3")
        self.som_morte = pygame.mixer.Sound("Assets/sfx_die.mp3")  # Novo som de morte

    def carregar_textura(self, caminho):
        imagem = Image.open(caminho).convert("RGBA")
        imagem = imagem.transpose(Image.FLIP_TOP_BOTTOM)
        img_data = imagem.tobytes()
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
        self.som_pulo.play()  # Reproduz o som do pulo

    def desenhar(self):
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.textura)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        glColor4f(1, 1, 1, 1)
        tamanho = 20
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex2f(self.x - tamanho, self.y - tamanho)
        glTexCoord2f(1, 0); glVertex2f(self.x + tamanho, self.y - tamanho)
        glTexCoord2f(1, 1); glVertex2f(self.x + tamanho, self.y + tamanho)
        glTexCoord2f(0, 1); glVertex2f(self.x - tamanho, self.y + tamanho)
        glEnd()

        glDisable(GL_BLEND)
        glDisable(GL_TEXTURE_2D)

    def colidiu_inferior(self, cano):
        bird_left = self.x - 15
        bird_right = self.x + 15
        bird_bottom = self.y - 15
        bird_top = self.y + 15

        pipe_left = cano.x
        pipe_right = cano.x + cano.largura
        pipe_bottom = 0
        pipe_top = cano.altura

        return not (bird_right < pipe_left or bird_left > pipe_right or bird_top < pipe_bottom or bird_bottom > pipe_top)

    def colidiu_superior(self, cano):
        bird_left = self.x - 15
        bird_right = self.x + 15
        bird_bottom = self.y - 15
        bird_top = self.y + 15

        pipe_left = cano.x
        pipe_right = cano.x + cano.largura
        pipe_bottom = cano.altura
        pipe_top = 600

        return not (bird_right < pipe_left or bird_left > pipe_right or bird_top < pipe_bottom or bird_bottom > pipe_top)
