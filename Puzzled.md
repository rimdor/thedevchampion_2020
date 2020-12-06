# Puzzled:
## Scripting [100 pts]
## Problème 
Nous avons intercepté ce fichier et nous savons qu'il contient quelque chose d'important, mais nos équipes n'ont pas réussi à trouvé quoi... Aidez nous à retrouver ce qu'il se cache dans ce fichier !  

[Fichier attaché](files/3pixels.csv)
## Résolution
On nous fournit un csv contenant la position des pixels et la valeur rgb de celui-ci dans cet ordre x, y, r, g, b. Nous utilisons donc le module Pillow en python pour dessiner l'image à partir de ces informations. J'ai également déterminé la hauteur et la largeur de l'image en analysant le csv puis en extrayant la valeur x maximale et la valeur y maximale. Nous n’avons pas utilisé le module csv pour analyser le fichier mais nous l’avons simplement traité comme un fichier normal. Voici notre script :
```python3
#!/usr/bin/python3

from PIL import Image

im = Image.new("RGB", (300, 41))
pix = im.load()

with open("3pixels.csv") as f:
    data = f.read()
    f.close()

data = data.split("\n")[1:]
#x = []
#y = []
#
#for i in data:
#    i = i.split(",")
#    x.append(int(i[0]))
#    y.append(int(i[1]))
#
#print(max(x))
#print(max(y))
for i in data:
    i = i.split(",")
    x = int(i[0])
    y = int(i[1])
    r = int(i[2])
    g = int(i[3])
    b = int(i[4])
    pix[x, y] = (r, g, b)

im.save("flag.png", "PNG")
```

## Flag

![Flag](/files/flag.png)
