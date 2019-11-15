"""
Week 2 Cour 2 Ex 5
Seekcha Sungkur
Q: Additionne 1 a chaque element impair d'une liste.
"""
text = input("Inserer les elements de votre list avec  , comme delimiteur: ")
list = text.split(",")
newList = []
n = 0

while n < len(list):
    x = int(list[n])
    if not x % 2 == 0:
        temp = x + 1
        newList.append(temp)
    else:
        newList.append(list[n])
    n += 1

m = 0
print("OLD  |  NEW\n")
while m < len(newList):
    print(str(list[m]) + " ==> " + str(newList[m]))
    m += 1
