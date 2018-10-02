import random
x = random.sample(range(100), 15)
y = random.sample(range(100), 20)
rlc=[]
print(x,'\n',y,'\n')
for a in x:
    for b in y:
        if a == b:
            rlc.append(a)
print(rlc)