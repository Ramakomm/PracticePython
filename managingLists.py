def makenewList(l):
    newList = []
    newList = [l[0],l[-1]]
    print(newList)

import random
list = random.sample(range(100), 15)
print(list)
makenewList(list)