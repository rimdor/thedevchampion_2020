# Typing
## Crypto [100 pts]
## Problème 
Nous avons intercepté une communication entre deux hackers recherchés, mais impossible de déchiffrer ce qu'ils se sont dit... Mais je suis sûr que vous ferez mieux que nos équipes !  

[Fichier attaché](files/2kia.txt)
## Résolution
C’est un code SMS multi-tap  
On décode avec :
```python3
abc_multitab_char = "8 44 444 7777 0 222 666 6 6 88 66 444 222 2 8 444 666 66 0 444 7777 0 666 66 33 0 44 88 66 3 777 33 3 0 7 33 777 222 33 66 8 0 7777 33 222 88 777 33 0 7777 666 0 444 0 222 2 66 0 7777 44 2 777 33 0 6 999 0 6 666 7777 8 0 7 777 33 222 444 666 88 7777 0 7777 33 222 777 33 8 0 3 33 888 222 44 2 6 7 11 8 33 66 1111 55 33 999 7777 1111 2 777 33 1111 33 66 666 88 4 44 111 0 3 666 0 66 666 8 0 7777 44 2 777 33 0 444 8 0 9 444 8 44 0 2 66 999 22 666 3 999 0 444 0 9 2 7777 0 8 666 555 3 0 8 44 444 7777 0 222 2 66 0 33 2 777 66 0 999 666 88 0 77 88 444 8 33 0 2 0 555 666 8 0 666 333 0 7 666 444 66 8 7777".split()
table_abc = {"2":"A",
             "22":"B",
             "222":"C",
             "3":"D",
             "33":"E",
             "333":"F",
             "4":"G",
             "44":"H",
             "444":"I",
             "5": "J",
             "55": "K",
             "555": "L",
             "6":"M",
             "66":"N",
             "666":"O",
             "7":"P",
             "77":"Q",
             "777":"R",
             "7777":"S",
             "8":"T",
             "88":"U",
             "888":"V",
             "9":"W",
             "99":"X",
             "999":"Y",
             "9999":"Z",
             "0":" ",
             "1":".",
             "11":"[",
             "111":"]",
             "1111":"_"
             }
flag = ""
for i in abc_multitab_char:
    flag+=table_abc[i]

print(flag)
```
## Flag
DEVCHAMP[TEN_KEYS_ARE_ENOUGH]
