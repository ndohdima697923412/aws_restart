tab=[1234,2676,2095,2097,399,4656,3624,2346,428,3637,4558,3984,9202,3733,232,448,658,335,4677,3678,3679,356,266,3863,89369,3683,63,838,3568]
maxValue=tab[0]
meanValue=0
for i in tab:
    if(i>maxValue):
        maxValue=i
print("Le plus grand element de votre tableau est: {}".format(maxValue))

for i in tab:
    meanValue=meanValue+i
meanValue=meanValue/len(tab)
print("La moyenne des valeurs de votre tableau est: {}".format(meanValue))    