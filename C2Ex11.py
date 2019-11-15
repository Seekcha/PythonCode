"""
Week 2 Cour 2 Ex 10
Seekcha Sungkur
Q: Un programme qui determine le plus petit multiple commun a deux nombres entier entres au clavier.
"""
n = int(input("inserer votre premier chiffre: "))
m = int(input("inserer votre deuxieme chiffre: "))

if n > m:
    big = n
else:
    big = m

while (True):
    if big % n == 0 and big % m == 0:
        num = big
        break
    big += 1

print("le numero est: " + str(num))