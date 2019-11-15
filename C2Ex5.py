"""
Week 2 Cour 2 Ex 5
Seekcha Sungkur
Q: Afficher 1 a n par etape (saut) de m.
"""
m = int(input("inserer votre chiffre a compter par etape: "))
n = int(input("inserer votre limite: "))

count = 1

while count <= n:
    print(count)
    count += m
