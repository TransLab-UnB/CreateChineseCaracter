from PIL import Image
import math

show = False

def unificarhorizontal(imagens_caminhos, output_path):
 imagens = [Image.open(img) for img in imagens_caminhos]

 largura_total = sum(img.width for img in imagens)
 altura_maxima = max(img.height for img in imagens)

 nova_imagem = Image.new('RGB', (largura_total, altura_maxima), (255, 255, 255))
 
 x_offset = 0
 for img in imagens:
     nova_imagem.paste(img, (x_offset, 0))
     x_offset += img.width
 
 nova_imagem.save(output_path)
 if show == True: nova_imagem.show()

def unificarvertical(imagens_caminhos, output_path):
 imagens = [Image.open(img) for img in imagens_caminhos]

 largura_total = max(img.width for img in imagens)
 altura_maxima = sum(img.height for img in imagens)

 nova_imagem = Image.new('RGB', (largura_total, altura_maxima), (255, 255, 255))
 
 x_offset = 0
 for img in imagens:
     nova_imagem.paste(img, (0, x_offset))
     x_offset += img.height
 
 nova_imagem.save(output_path)
 if show == True: nova_imagem.show()


def unificarquadrada(imagens_caminhos, output_path):

    imagens = [Image.open(img) for img in imagens_caminhos]

    largura_img, altura_img = imagens[0].size

    num_imagens = len(imagens)
    colunas = math.ceil(math.sqrt(num_imagens))  # Número de colunas
    linhas = math.ceil(num_imagens / colunas)    # Número de linhas

    largura_total = colunas * largura_img
    altura_total = linhas * altura_img
    nova_imagem = Image.new('RGB', (largura_total, altura_total), (255, 255, 255))

    for idx, img in enumerate(imagens):
        x = (idx % colunas) * largura_img
        y = (idx // colunas) * altura_img
        nova_imagem.paste(img, (x, y))

    nova_imagem.save(output_path)
    if show == True: nova_imagem.show()
