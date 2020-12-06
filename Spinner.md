# Spinner
## Reverse Engineering [100 pts]
## Problème 
Merci d'avoir trouvé le premier mot de passe ! Mais nous sommes de nouveau bloqués par un autre mot de passe... Pouvez-vous le retrouver ?  
[Fichier attaché](files/2spinner.py)
## Résolution
On transforme l’output en binaire, et on le splite en des blocs de 7 bits, ensuite on fait le travail en inverse pour avoir le flag :  
```python3
import binascii
a=bin(6838670745825122932886199347866255930502612544243548566773595)
z = [a[i:i+7] for i in range(2, len(a), 7)]
i = 0
f = ''
d = ""
for c in z:
    d += chr(int(c[-i:] + c[:-i],2))
    i = (i + 1) % 8
print(d)

```

## Flag

DEVCHAMP[my_head_is_spinning]
