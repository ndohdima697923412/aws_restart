import random


print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number=random.randint(1,10)
isGuessRigth= False
while isGuessRigth != True:
    guess = input("Guess the number between 1 and 10 : ")
    if int(guess)==number:
        print("Vous avez deviné le nombre")
        isGuessRigth=True
    else:
        print("Le nombre est incorrect veillez reessayer")
        
for x in range(1,10):
    print(x)