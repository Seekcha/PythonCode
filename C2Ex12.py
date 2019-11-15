"""
Week 2 Cour 2 Ex 10
Seekcha Sungkur
Q: Un programme qui affiche 'Acces refuse' tant que lw nom d'utilisateur et mot de passe sont incorrectes.
"""
pswd = "deeya"
nom = "deeya"

inom = input("veuillez inserer votre nom: ")
ipswd = input("veuillez inserer le mot de pass: ")

acces = False

while not acces:
    if inom == nom and ipswd == pswd:
        print("bienvenu")
        acces = True
    else:
        print("\nErreur veuillez re essayer svp\n")
        inom = input("veuillez inserer votre nom")
        ipswd = input("veuillez inserer le mot de pass")