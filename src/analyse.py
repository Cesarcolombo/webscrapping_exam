import json

with open("data.json", "r", encoding="utf-8") as f:
    donnee = json.load(f)

# Tu peux maintenant utiliser donnee
compteur = {}
    
for element in donnee:
    # element est de la forme [citation, [tag1, tag2, ...]]
    tags = element[1] 
        
    for tag in tags:
        if tag in compteur:
            compteur[tag] += 1
        else:
            compteur[tag] = 1
                

print(compteur)