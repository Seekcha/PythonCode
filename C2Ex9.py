"""
Week 2 Cour 2 Ex 9
Seekcha Sungkur
Q: Lire un fichier contenant 5 lignes et afficher chaque ligne en prefixant par son numpro de ligne et le nbr de caracteres(ex 1. Premiere ligne: [14])
"""
m = open("list.txt","r")
aList = m.readlines()

count = 0

while count < len(aList):
    print("ligne " + str(count) + " contient: " + aList[count] + " et contient " + str(len(aList[count])) + " carateres")
    count += 1

