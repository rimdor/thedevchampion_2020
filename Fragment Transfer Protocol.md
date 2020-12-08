# Fragment Transfer Protocol
## Network [125 pts]
## Problème 
À cause d'une erreur de configuration, un attaquant a pu se connecter à notre serveur FTP et voler des données confidentielles. Trouvez ce que contenaient le fichier volé afin que nous prenions les mesures nécessaires.  

[Fichier attaché](files/capture.pcapng)
## Résolution
Avec wireshark, le 46e paquet utilisant le protocol ftp-data et traite d'un certain flag.png, il fallait le voir de prêt. Clique droit;  Suivre; FTP stream  
![](files/stream.png)
On voit le header du PNG,  
![](files/raw.png)  
On change vers RAW, on enregistre sous un fichier png.  
## Flag
![](files/fragflag.png)
