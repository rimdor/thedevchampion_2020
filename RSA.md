# RSA
## Crypto [125 pts]
## Problème 
Nous avons réussi à intercepter les communications d'un grand criminel, mais elles sont chiffrées. 
Nos équipes travaillent depuis des mois à les déchiffrer, mais une pièce manque pour avoir la clé complète... 
Il suffirait de retrouver le nombre x tel que : x ^ 65537 mod 120701443617098609 = 37155663075427 Pouvez vous nous aider ? 
Soumettez votre solution au format DEVCHAMP[x]  

## Résolution
Un challenge typique de rsa.
On note de l'explication que `n=120701443617098609`, `C=37155663075427` et `e = 65537`
Avec l'outil [http://factordb.com/](http://factordb.com/). Nous factorisons `n` puis calculons la clé privé `d`. Voici le script:

```python3

from Crypto.Util.number import inverse
p,q = 31424117, 3841044877
n = 120701443617098609 
phi_n = (p-1) * (q-1)

d = inverse(65537, phi_n)

print pow(37155663075427, d, n)
```

## Flag
DEVCHAMP[3898582264549172]
