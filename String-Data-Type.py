myString="This is my String"
print(myString)
print(type(myString))
print(myString+"Is of the data type "+str(type(myString)))

firstString="Water"
secondString="fall"
thirdString=firstString+secondString
print(thirdString)

name=input("What is your name? ")
print(name)

color=input("What is your favorite color? ")
animal=input("What is your favorite animal? ")
print("{}, you look like a {} {}!".format(name,color,animal))
