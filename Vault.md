# Vault
## Reverse Engineering [50 pts]
## Problème 
Nous avons trouvé une plateforme de stockage de fichiers dangereux, mais un étrange système d'authentification nous barre le chemin... Trouvez le mot de passe valide !  

[Fichier attaché](files/1vault.py)
## Résolution
Problème facile, on remplace les “==” avec “=” :
```python3
user_input = [""] * 55
user_input[34] = "h" 
user_input[28] = "o" 
user_input[24] = "n" 
user_input[2] = "V" 
user_input[50] = "3" 
user_input[20] = "k" 
user_input[4] = "H" 
user_input[30] = "3" 
user_input[11] = "h" 
user_input[23] = "_" 
user_input[46] = "3" 
user_input[5] = "A" 
user_input[41] = "s" 
user_input[40] = "e" 
user_input[42] = "_" 
user_input[52] = "s" 
user_input[26] = "w" 
user_input[12] = "a" 
user_input[43] = "4" 
user_input[35] = "e" 
user_input[27] = "_" 
user_input[18] = "3" 
user_input[0] = "D" 
user_input[7] = "P" 
user_input[32] = "_" 
user_input[1] = "E" 
user_input[17] = "h" 
user_input[14] = "e" 
user_input[9] = "I" 
user_input[16] = "t" 
user_input[54] = "]" 
user_input[8] = "[" 
user_input[47] = "_" 
user_input[53] = "e" 
user_input[29] = "p" 
user_input[48] = "p" 
user_input[44] = "_" 
user_input[45] = "m" 
user_input[25] = "0" 
user_input[10] = "_" 
user_input[51] = "4" 
user_input[13] = "v" 
user_input[31] = "n" 
user_input[37] = "g" 
user_input[39] = "t" 
user_input[19] = "_" 
user_input[3] = "C" 
user_input[36] = "_" 
user_input[15] = "_" 
user_input[22] = "y" 
user_input[6] = "M" 
user_input[38] = "4" 
user_input[33] = "t" 
user_input[49] = "l" 
user_input[21] = "e"

print("".join(user_input))

```

## Flag

DEVCHAMP[I_have_th3_key_n0w_op3n_the_g4tes_4_m3_pl34se]
