tab=[]
number=input("Entrer un nombre et le programme vous dira s'il est pair ou impair ")
tab.append(int(number))
print(tab)
for i in tab:
    if (i%2==0):
        print("Votre nombre est pair")
    else: 
        print("Votre nombre est impair")

