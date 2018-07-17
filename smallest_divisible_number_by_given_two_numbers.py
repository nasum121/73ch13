L,R=input().split()
L=int(L)
R=int(R)
lis=[]
for i in range(1,100000):
    if i%L==0 and i%R==0:
        lis.append(i)
print(lis[0])
