from PIL import Image, ImageDraw, ImageFont

def generate_chinese_char_image(unicode_char, dimension, font_path, output_path):
    # Cria uma imagem em branco com as dimensões especificadas
    img = Image.new("RGB", (dimension, dimension+1), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Carrega a fonte com um tamanho adequado para a imagem
    try:
        font_size = dimension # ajusta o tamanho da fonte
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print("Fonte não encontrada ou falha ao carregar.")
        return

    # Texto a ser desenhado
    text = chr(unicode_char)

    # Obtém as coordenadas da caixa delimitadora do texto
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Calcula a posição para centralizar o caractere
    position = ((dimension - text_width) // 2, (dimension - text_height) // 2)

    # Desenha o caractere na imagem
    draw.text(position, text, font=font, fill=(0, 0, 0))

    # Salva a imagem
    img.save(output_path)

    print(f"Imagem gerada e salva em {output_path}")

def generate_chinese_char_image_sung(unicode_char, dimension, output_path):
    font_path = "Fonts_Sung/TW-Sung-98_1.ttf"  # Caminho para a fonte Sung
    generate_chinese_char_image(unicode_char, dimension, font_path, output_path)


def generate_chinese_char_image_kai(unicode_char, dimension, output_path):
    font_path = "Fonts_Kai/TW-Kai-98_1.ttf"  # Caminho para a fonte Kai
    generate_chinese_char_image(unicode_char, dimension, font_path, output_path)


# Parâmetros para gerar a imagem
#unicode_char = 0x7D44  # Unicode para o caractere chinês (汉)
#dimension = 96  # Tamanho da imagem (512x512)
#font_path = "Fonts_Sung/TW-Sung-98_1.ttf"  # Caminho para a fonte Sung
#font_path = "Fonts_Kai/TW-Kai-98_1.ttf"
#output_path = f"7D44_{dimension}_gerado_kai.png"  # Caminho para salvar a imagem
#generate_chinese_char_image(unicode_char, dimension, font_path, output_path)
