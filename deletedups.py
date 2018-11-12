def delDups(list):
    list1 =[]
    for i in list:
        if i not in list1:
            list1.append(i)
    return list1
import random
#list = random.sample(range(100),20)
list = [10,67,10,68,47,90]
#print(list)
ls = delDups(list)
print(ls)



