# Hack the Week
## Scripting [50 pts]
## Problème 
Nous avons mis sur écoute il y a plusieurs années un hacker recherché. Nous avons la liste de toutes ses connexions à son ordinateur. Nous pensons qu'il va réaliser son prochain hack mercredi prochain, mais nous voulons être sûr que le mercredi est bien son jour favori.

A partir de la liste de jours données dans le fichier, trouvez le nombre de lignes qui correspondent à un mercredi. Entrez le flag sous la forme DEVCHAMP[123] si vous pensez qu'il y a 123 mercredis.  
[Fichier attaché](files/1weekdays.txt)
## Resolution
On savait combien de mercredis il y a dans les dates de connexion à l'ordinateur, en utilisant le module datetime en python et en convertissant les dates des chaînes en objets de date qui correspondent à un calendrier contenant les bons numéros de jour de toutes les années passées. Puis en convertissant chaque objet en une chaîne contenant le nom du jour de la semaine. On compte le nombre de mercredi qu'il y avait dans la liste générée. Le script :
```python
#!/usr/bin/python3

from datetime import datetime

with open("1weekdays.txt") as f:
    data = f.read()
    f.close()

print([datetime.strptime(_, "%d/%m/%Y").strftime("%A") for _ in data.split("\n")].count("Wednesday"))
```
