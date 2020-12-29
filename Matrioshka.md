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




## Flag

