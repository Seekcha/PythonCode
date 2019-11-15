"""
Week 2 Cour 2 Ex 10
Seekcha Sungkur
Q: Ameliorer le script (2) pour sauvegarder le resultat dans un fichier 'multi.txt'
"""
text = input("Veuillez inserer un text: ")

print("Votre text est: " +str(text))

output = open("mult.txt","w")
newText = ""
count = 0
voyelle = 0
while count < len(text):
    if text[count].lower() ==  "a" or text[count].lower() ==  "e" or text[count].lower() ==  "i" or text[count].lower() ==  "o" or text[count].lower() ==  "u":
        voyelle += 1
        newText += text[count] + " "
    count += 1

output.write("Les voyelles sont: " +str(newText))
