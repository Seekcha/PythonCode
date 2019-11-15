"""
Week 2 Cour 2 Ex 4
Seekcha Sungkur
Q: Modifiez le programme (3) pour afficher la table de 1 a m
"""
n = int(input("inserer votre table de multiplication: "))
m = int(input("inserer votre limite de multiplication: "))

count = 1

while count <= m:
    print(str(count) + " X " + str(n) + " = " + str(count*n))
    count +=1