from PIL import Image
from OpenGL.GL import *

textura_fundo = None
fundo_largura = 0
fundo_altura = 0

def carregar_textura_fundo(caminho):
    global textura_fundo, fundo_largura, fundo_altura

    imagem = Image.open(caminho).transpose(Image.FLIP_TOP_BOTTOM)
    img_data = imagem.convert("RGB").tobytes()
    fundo_largura, fundo_altura = imagem.size

    textura_fundo = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textura_fundo)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, fundo_largura, fundo_altura, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)

def desenhar_fundo(pos, altura):
    global textura_fundo, fundo_largura

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textura_fundo)

    for i in range(2):
        x = (pos + i * fundo_largura) % (2 * fundo_largura) - fundo_largura
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex2f(x, 0)
        glTexCoord2f(1, 0)
        glVertex2f(x + fundo_largura, 0)
        glTexCoord2f(1, 1)
        glVertex2f(x + fundo_largura, altura)
        glTexCoord2f(0, 1)
        glVertex2f(x, altura)
        glEnd()

    glDisable(GL_TEXTURE_2D)

