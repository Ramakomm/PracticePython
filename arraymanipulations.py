import array as arr
import sys
sys.path.append("numpy_path")
import numpy as np
a = arr.array('i',[10,67,38,92,84])
#Deleting an element f an array
ind = int(input("give the index of the array element that should be removed\n"))
if ind > len(a):
    print("Index out of bounds")
del a[ind]

print(a)
def reverseArray(a):
    reversedArray= a[::-1]
    print(reversedArray)
reverseArray(a)
