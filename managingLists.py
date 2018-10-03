def makenewList(l):
    newList = []
    newList.append(l[0])
    newList.append(l[-1])
    print(newList)

import random
list = random.sample(range(100), 15)
print(list)
makenewList(list)