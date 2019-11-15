"""
Week 2 Cour 2 Ex 7
Seekcha Sungkur
Q: Compter les nombres de voyelles dans un texte.
"""

text = input("Veuillez inserer un text: ")

print("Votre text est: " +str(text))
count = 0
voyelle = 0
while count < len(text):
    if text[count].lower() == "a" or text[count].lower() == "e" or text[count].lower() == "i" or text[count].lower() == "o" or text[count].lower() == "u":
        voyelle += 1
    count += 1

if voyelle == 0:
    print("Aucune voyelle")
else:
    print("le nombre de voyelle est: " + str(voyelle))

