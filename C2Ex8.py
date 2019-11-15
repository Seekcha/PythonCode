"""
Week 2 Cour 2 Ex 8
Seekcha Sungkur
Q: Modifiez le programme ci-dessus pour afficher les voyelles dans le texte en gras.
"""
text = input("Veuillez inserer un text: ")

print("Votre text est: " +str(text))

newText = ""

m = "\033[1m"
n = "\033[0m"

count = 0
voyelle = 0
while count < len(text):
    if text[count].lower() == "a" or text[count].lower() == "e" or text[count].lower() == "i" or text[count].lower() == "o" or text[count].lower() == "u":
        voyelle += 1
        newText += m + text[count] + n
    else:
        newText += text[count]
    count += 1

if voyelle == 0:
    print("Aucune voyelle")
else:
    print("le nombre de voyelle est: " + str(voyelle))

## use loop to concatenate text
print("votre nouveau text est " + str(newText))
