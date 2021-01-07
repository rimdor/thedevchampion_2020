# Matrioshka
## Reverse Engineering [125 pts]
## Problème 
Il semblerait que nous arrivons proche du but, plus qu'un mot de passe à trouver ! Celui-ci semble encore plus dur à trouver que le précédent, mais nous avons confiance en vous.

[Fichier attaché](files/3matrioshka.py)

## Résolution
Observons de prêt ici:

```python3
def check(s):
    if len(s)!= 30 or 'XHFS%~p8#j:&ih<jim~NYFj5i!oEX%' != f6(f6(f2(f1(f7(f10(f5(f5(f6(f7(f6(f8(f2(f9(f8(f6(f5(f6(f2(f6(f7(f3(f3(f5(f2(f2(f2(f8(f2(f1(f10(f4(f8(f5(f5(f8(f2(f9(f2(f5(f3(f7(f8(f3(f4(f5(f10(f4(f1(f9(s)))))))))))))))))))))))))))))))))))))))))))))))))):
        print('Nope')
    else:
        print('OK!')

check(input('Enter the flag: '))
```
Nous notons que le flag est composé de 30 caractères de sorte que ![formula](https://render.githubusercontent.com/render/math?math=(f6%20\circ%20f6%20\circ%20f2%20\circ%20f1%20\circ%20f7%20\circ%20f10%20\circ%20f5%20\circ%20f5%20\circ%20f6%20\circ%20f7%20\circ%20f6%20\circ%20f8%20\circ%20f2%20\circ%20f9%20\circ%20f8%20\circ%20f6%20\circ%20f5%20\circ%20f6%20\circ%20f2%20\circ%20f6%20\circ%20f7%20\circ%20f3%20\circ%20f3%20\circ%20f5%20\circ%20f2%20\circ%20f2%20\circ%20f2%20\circ%20f8%20\circ%20f2%20\circ%20f1%20\circ%20f10%20\circ%20f4%20\circ%20f8%20\circ%20f5%20\circ%20f5%20\circ%20f8%20\circ%20f2%20\circ%20f9%20\circ%20f2%20\circ%20f5%20\circ%20f3%20\circ%20f7%20\circ%20f8%20\circ%20f3%20\circ%20f4%20\circ%20f5%20\circ%20f10%20\circ%20f4%20\circ%20f1%20\circ%20f9)(flag)) soit égal à `XHFS%~p8#j:&ih<jim~NYFj5i!oEX%`.  

Soit ![formula](https://render.githubusercontent.com/render/math?math=g=(f6%20\circ%20f6%20\circ%20f2%20\circ%20f1%20\circ%20f7%20\circ%20f10%20\circ%20f5%20\circ%20f5%20\circ%20f6%20\circ%20f7%20\circ%20f6%20\circ%20f8%20\circ%20f2%20\circ%20f9%20\circ%20f8%20\circ%20f6%20\circ%20f5%20\circ%20f6%20\circ%20f2%20\circ%20f6%20\circ%20f7%20\circ%20f3%20\circ%20f3%20\circ%20f5%20\circ%20f2%20\circ%20f2%20\circ%20f2%20\circ%20f8%20\circ%20f2%20\circ%20f1%20\circ%20f10%20\circ%20f4%20\circ%20f8%20\circ%20f5%20\circ%20f5%20\circ%20f8%20\circ%20f2%20\circ%20f9%20\circ%20f2%20\circ%20f5%20\circ%20f3%20\circ%20f7%20\circ%20f8%20\circ%20f3%20\circ%20f4%20\circ%20f5%20\circ%20f10%20\circ%20f4%20\circ%20f1%20\circ%20f9)) et  ![formula](https://render.githubusercontent.com/render/math?math=y=) `XHFS%~p8#j:&ih<jim~NYFj5i!oEX%`.
Ainsi notre flag est la chaine de caractères telle que ![formula](https://render.githubusercontent.com/render/math?math=g(flag)=y) .  
Il est alors question de déterminer ![formula](https://render.githubusercontent.com/render/math?math=g^{-1}) tel que ![formula](https://render.githubusercontent.com/render/math?math=g^{-1}(y)=flag).  
![formula](https://render.githubusercontent.com/render/math?math=g^{-1}) est défini par ![formula](https://render.githubusercontent.com/render/math?math=f9^{-1}%20\circ%20f1^{-1}%20\circ%20f4^{-1}%20\circ%20f10^{-1}%20\circ%20f5^{-1}%20\circ%20f4^{-1}%20\circ%20f3^{-1}%20\circ%20f8^{-1}%20\circ%20f7^{-1}%20\circ%20f3^{-1}%20\circ%20f5^{-1}%20\circ%20f2^{-1}%20\circ%20f9^{-1}%20\circ%20f2^{-1}%20\circ%20f8^{-1}%20\circ%20f5^{-1}%20\circ%20f5^{-1}%20\circ%20f8^{-1}%20\circ%20f4^{-1}%20\circ%20f10^{-1}%20\circ%20f1^{-1}%20\circ%20f2^{-1}%20\circ%20f8^{-1}%20\circ%20f2^{-1}%20\circ%20f2^{-1}%20\circ%20f2^{-1}%20\circ%20f5^{-1}%20\circ%20f3^{-1}%20\circ%20f3^{-1}%20\circ%20f7^{-1}%20\circ%20f6^{-1}%20\circ%20f2^{-1}%20\circ%20f6^{-1}%20\circ%20f5^{-1}%20\circ%20f6^{-1}%20\circ%20f8^{-1}%20\circ%20f9^{-1}%20\circ%20f2^{-1}%20\circ%20f8^{-1}%20\circ%20f6^{-1}%20\circ%20f7^{-1}%20\circ%20f6^{-1}%20\circ%20f5^{-1}%20\circ%20f5^{-1}%20\circ%20f10^{-1}%20\circ%20f7^{-1}%20\circ%20f1^{-1}%20\circ%20f2^{-1}%20\circ%20f6^{-1}%20\circ%20f6^{-1})  

Il nous revient de determiner l'inverse de chaque fonction.
En analysant des fonctions, nous réalisons tout de suite que ![formula](https://render.githubusercontent.com/render/math?math=f1) inverse la chaîne qu'elle reçoit. Ainsi  ![formula](https://render.githubusercontent.com/render/math?math=f1^{-1}=f1). Une analyse pareille pour chacune des fonctions nous permet d'aboutir à la même conclusion pour ![formula](https://render.githubusercontent.com/render/math?math=f9,%20f8,%20f7%20et%20f3).  
Reste juste à trouver l’inverse de f2, f5, f4, f6 et f10.  
Nous nous rendons aussi compte que ![formula](https://render.githubusercontent.com/render/math?math=f4) est l'inverse de ![formula](https://render.githubusercontent.com/render/math?math=f5) et reciproquement.

La détermination de l'inverse de la fonction ![formula](https://render.githubusercontent.com/render/math?math=f10) s'avère la plus facile et donne:
```python3
def f10(s):
    return s[1:] + s[0]
```
Reste à déterminer ![formula](https://render.githubusercontent.com/render/math?math=f2) et ![formula](https://render.githubusercontent.com/render/math?math=f6), voici l’inverse de ![formula](https://render.githubusercontent.com/render/math?math=f2):

```python3
def f2(x):
    y = x[:(len(x)//2)]
    z = x[(len(x)//2):]
    res = [_ for _ in range(len(x))]

    count = 0
    for i in range(len(y)):
        res[count] = y[i]
        count += 2

    count = 1
    for i in range(len(z)):
        res[count] = z[i]
        count += 2

    res = "".join(res)
    return res
```

Et pour l’inverse de ![formula](https://render.githubusercontent.com/render/math?math=f6), on sait que les indexes générées sont fixés chaque fois alors on génère une table de correspondance et on l’inverse, en utilisant ce script:

```python3
def f6(s):
    r = ''
    idx = 1
    for i in range(30):
        idx *= 11
        idx %= 31
        r += s[idx-1]
    return r

import string

x = string.ascii_lowercase + "0123"
img = f6(string.ascii_lowercase + "0123")
d = {}
for i,c in enumerate(img):
    d[x.find(c)] = i
#print(d)
oo = ""
print(d)
for i,c in enumerate(img):
    oo += img[d[i]]
print(oo)
```

Voici l’inverse de ![formula](https://render.githubusercontent.com/render/math?math=f6):

```python3
def f6(s):
    d = {0: 29, 1: 17, 2: 16, 3: 5, 4: 9, 5: 4, 6: 25, 7: 23, 8: 3, 9: 27, 10: 0, 11: 22, 12: 6, 13: 13, 14: 26, 15: 11, 16: 28, 17: 21, 18: 7, 19: 15, 20: 12, 21: 18, 22: 8, 23: 10, 24: 19, 25: 24, 26: 20, 27: 1, 28: 2, 29: 14}

    r = ''
    for i in range(len(s)):
        r += s[d[i]]
    return r
```

Ainsi nous avons l'inverse de toutes les fonctions, en recap nous avons:
```python3
def f1(s):
    return s[::-1]

def f2(x):
    y = x[:(len(x)//2)]
    z = x[(len(x)//2):]
    res = [_ for _ in range(len(x))]

    count = 0
    for i in range(len(y)):
        res[count] = y[i]
        count += 2

    count = 1
    for i in range(len(z)):
        res[count] = z[i]
        count += 2

    res = "".join(res)
    return res


def f3(s):
    r = ''
    for c in s:
        r += chr(ord(c) ^ 0xf)
    return r

def f5(s):
    r = ''
    for c in s:
        r += chr(ord(c) - 1 if ord(c) != 32 else 126)
    return r

def f4(s):
    r = ''
    for c in s:
        r += chr(ord(c) + 1 if ord(c) != 126 else 32)
    return r

def f6(s):
    d = {0: 29, 1: 17, 2: 16, 3: 5, 4: 9, 5: 4, 6: 25, 7: 23, 8: 3, 9: 27, 10: 0, 11: 22, 12: 6, 13: 13, 14: 26, 15: 11, 16: 28, 17: 21, 18: 7, 19: 15, 20: 12, 21: 18, 22: 8, 23: 10, 24: 19, 25: 24, 26: 20, 27: 1, 28: 2, 29: 14}
    r = ''
    for i in range(len(s)):
        r += s[d[i]]
    return r

def f7(s):
    return s.swapcase()

def f8(s):
    r = ''
    for c in s:
        if 'a'<=c<='z':
            r += chr((ord(c)-ord('a') + 13)%26 + ord('a'))
        else:
            r += c
    return r

def f9(s):
    r = ''
    for c in s:
        if 'A'<=c<='Z':
            r += chr((ord(c)-ord('A') + 13)%26 + ord('A'))
        else:
            r += c
    return r

def f10(s):
    return s[1:] + s[0]


z = 'XHFS%~p8#j:&ih<jim~NYFj5i!oEX%'
flag = f9(f1(f4(f10(f5(f4(f3(f8(f7(f3(f5(f2(f9(f2(f8(f5(f5(f8(f4(f10(f1(f2(f8(f2(f2(f2(f5(f3(f3(f7(f6(f2(f6(f5(f6(f8(f9(f2(f8(f6(f7(f6(f5(f5(f10(f7(f1(f2(f6(f6(z))))))))))))))))))))))))))))))))))))))))))))))))))
print(flag)
```


## Flag

#DEVCHAMP[Ne5tEd_NEs73D_D0lls!]
