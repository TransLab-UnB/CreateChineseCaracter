from unificarimagem import unificarhorizontal, unificarvertical, unificarquadrada

dimension = [12, 16, 24, 32, 35, 36, 48, 56, 60, 96]
dimension = [96]
radical = ["4ebb", "624c", "8279", "56d7"]
component = ["65b9", "7528", "7530", "53e4"]
char = ["4eff", "62e5", "82d7", "56fa"]

raiz = f"matriz2x2/"
radicalimg = []
radicalimage = raiz + 'radical/'
componentimg = []
componentimage = raiz + 'component/'


for i in range (0,len(radical)):
  radicalimg.append(raiz + 'radical/' + radical[i] + '_sung.png')
  radicalimage = radicalimage + radical[i] + '_'

for i in range (0,len(component)):
  componentimg.append(raiz + 'component/' + component[i] + '_sung.png')
  componentimage = componentimage + component[i] + '_'


for d in dimension:
  unificarhorizontal([s.replace("matriz2x2/", f"matriz2x2/{d}/") for s in radicalimg], (radicalimage + 'h.png').replace("matriz2x2/", f"matriz2x2/{d}/"))
  unificarvertical([s.replace("matriz2x2/", f"matriz2x2/{d}/") for s in radicalimg], (radicalimage + 'v.png').replace("matriz2x2/", f"matriz2x2/{d}/"))
  unificarquadrada([s.replace("matriz2x2/", f"matriz2x2/{d}/") for s in radicalimg], (radicalimage + 'q.png').replace("matriz2x2/", f"matriz2x2/{d}/"))

  unificarhorizontal([s.replace("matriz2x2/", f"matriz2x2/{d}/") for s in componentimg], (componentimage + 'h.png').replace("matriz2x2/", f"matriz2x2/{d}/"))
  unificarvertical([s.replace("matriz2x2/", f"matriz2x2/{d}/") for s in componentimg], (componentimage + 'v.png').replace("matriz2x2/", f"matriz2x2/{d}/"))
  unificarquadrada([s.replace("matriz2x2/", f"matriz2x2/{d}/") for s in componentimg], (componentimage + 'q.png').replace("matriz2x2/", f"matriz2x2/{d}/"))