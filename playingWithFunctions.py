from Listinglists import *
def person(**data):
    for i,j in data.items():
        print(i,j)
person(age=23,name='rama',city = "khammam",job = "SE")
def countevenodd(lis):
    even = 0
    odd = 0
    for i in lis:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    return odd, even
odd, even = countevenodd([11,2,3,4,5,6,7,8,9,19])
print(odd,even)

lis = getUsernames()
#lis1 = usernamelen(lis)
def fact(n):
    if n == 0 or n ==1:
        return 1

    return n * fact(n-1)
p = fact(4)
print(p)
f = lambda a : a**3
print(f(7))
print(hex(34))