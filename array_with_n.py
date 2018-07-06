a,b=input().split()
a=int(a)
b=int(b)
list=[]
su=0
for i in range(a):
    list.append(i+1)
print (list)
for j in range(b):
    su=list[j]+su
print (su)
    


