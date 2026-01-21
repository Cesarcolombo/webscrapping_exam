import json
import matplotlib.pyplot as plt

# on récupère les données
with open("data.json", "r", encoding="utf-8") as f:
    donnee = json.load(f)

# on recrée le dictionnaire compteur
compteur = {}
for element in donnee:
    tags = element[1]
    for tag in tags:
        if tag in compteur:
            compteur[tag] += 1
        else:
            compteur[tag] = 1

# pour ne garder que les tags apparaissant au moins deux fois
liste_tags = []
liste_counts = []

for tag, nombre in compteur.items():
    if nombre > 2:
        liste_tags.append(tag)
        liste_counts.append(nombre)

# création du graph
plt.figure(figsize=(10, 6))  # on agrandit un peu la fenêtre
plt.bar(liste_tags, liste_counts)

# on tourne les labels pour qu'ils soient lisibles
plt.xticks(rotation=90) 
plt.ylabel("Nombre d'apparitions")
plt.title("Fréquence des tags (> 2 apparitions)")

plt.show()
