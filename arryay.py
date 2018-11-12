import array as arr
vals = arr.array('i',[6,7,8,9,10,11,57,2,5,67])
for i in range(len(vals)):
    for j in range(i+1,len(vals)):
        if vals[i]>vals[j]:
            temp = vals[i]
            vals[i] = vals[j]
            vals[j] = temp


print(vals)
def fact(num):
    prod = 1
    for i in range(1,num):
        prod = prod * i
        #print(prod)

    print (prod)
#fact(10)

vals = arr.array('i',[])
maxlen = int(input("Give us the length of the array\n"))
for i in range(maxlen):
    x = int(input("Enter the first element"))
    vals.append(x)
print(vals)
num = input("enter the number to count\n")
k = 0
for e in vals:
    if e == num:
        print(e,num)
        print(k)
        break
    k = k + 1
print(vals)
print(k,vals.index(num))



