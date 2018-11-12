def cubingnumber(t):
    return t ** 3
def numbersense(num):
    if num > 0 :
        print("posiitive")
    else:
        print("negative")
def findGreatest(lis):
    greatest = 0
    for i in lis:
        if i > greatest :
            greatest = i
    print(greatest)
def febnoci(num):
    fblist = [0,1,1]
    i = 2
    while(i<=num):
        fblist.append(fblist[i]+fblist[i-1])
        i+=1
    print(fblist)
febnoci(50)

#while (True):
    #num = int(input("Give the number for which you need fing the cube \n"))
    #print(cubingnumber(num))
    #num,num1,num2 = map(int,input("give any 3 numbers with space\n").split())
    #numbersense(num)
   # lis = [345,5776,38895,67799,38,679]
    #findGreatest(lis)
    #choice = int(input("Press 0 to Quit\n"))
    #if choice== 0 :
    #    break

i = 0
while (i<=100):
    if (i % 3 == 0) or (i % 5 == 0):
        i = i +1
        continue
    print (i)
    i = i + 1
i = 0
while (i<5):
    print("# # # # #")
    i = i + 1
for i in range(1, int(500 ** 0.5 + 1)):

        print(i," ",i**2)
for j in range(4):
    for i in range(4-j):
        print(j+i+1 ," ",end="")
    print()











