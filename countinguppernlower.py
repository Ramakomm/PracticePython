import string
def countingLowernUpper(strin):
    countUpper =0
    countLower =0
    for i in strin:
        if (i.isupper()):
            countUpper = countUpper + 1
        elif (i.islower()):
            countLower = countLower + 1
        else:
            pass

    print("Upper Case letters Count are " + str(countUpper)+"\n")
    print("Lower Case letters Count are " + str(countLower) + "\n")
def sumOfList(lis):
    sum = 0
    for i in lis:
        sum = sum + i
    return sum
listw = [100, 200, 300, 400, 0, 500]
#countingLowernUpper('Tutorials POINT')
print(sumOfList(listw))

