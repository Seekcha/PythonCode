"""
Week 2 Cour 2 Ex 3
Seekcha Sungkur
Q: Un programme qui permet d'afficher la table de multiplication de n
"""
n = int(input("inserer votre table de multiplication: "))

count = 1

while count <= 12:
    print(str(count) + " X " + str(n) + " = " + str(count*n))
    count += 1