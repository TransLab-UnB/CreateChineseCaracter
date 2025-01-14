from geradorCaracter import generate_chinese_char_image_sung 

dimension = [12, 16, 24, 32, 35, 36, 48, 56, 60, 96]
radical = ["4ebb", "624c", "8279", "56d7"]
component = ["65b9", "7528", "7530", "53e4"]
char = ["4eff", "62e5", "82d7", "56fa"]

for d in dimension:
 for i in range (0,4):
  unicode_char = int(radical[i], 16)
  output_path = f"matriz2x2/{d}/radical/{radical[i]}_sung.png"  # Caminho para salvar a imagem
  generate_chinese_char_image_sung(unicode_char, d, output_path)

 for i in range (0,4):
  unicode_char = int(component[i], 16)
  output_path = f"matriz2x2/{d}/component/{component[i]}_sung.png"  # Caminho para salvar a imagem
  generate_chinese_char_image_sung(unicode_char, d, output_path)

 for i in range (0,4):
  unicode_char = int(char[i], 16)
  output_path = f"matriz2x2/{d}/char/{char[i]}_sung.png"  # Caminho para salvar a imagem
  generate_chinese_char_image_sung(unicode_char, d, output_path)