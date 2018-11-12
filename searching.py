def sortedLis(lis):
    temp = 0
    for i in range(len(lis)):
        for j in range(i+1,len(lis)):
            if lis[i] > lis[j] :
                temp = lis[i]
                lis[i] = lis[j]
                lis[j] = temp
    print(lis)
#sortedLis([237,5,1,54,7,8,9,10])

def searchNum(lis,num):
    sortedLis(lis)
    while(True):
        index= int(len(lis)/2)
        if(index< 0):
            break

        if(num == lis[index]):
            print("found the number",num)
            break
        elif(num<lis[index]):
            lis = lis[0:index:]
            continue
        else:
            lis = lis[index:]
            continue



searchNum([100,3141,588,676,4,39,8],676)



