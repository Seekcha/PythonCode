"""
Week 2 Cour 2 Ex 2
Seekcha Sungkur
Q: Modifiez le programme (1) pour afficher seulement le chiffre pair.
"""
x = int(input("inserez un numero: "))

count = 1

while count <= x:
    if count % 2 == 0:
        print(count)
    count += 1