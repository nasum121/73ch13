n,k=input().split()
n=int(n)
k=int(k)
list1=[]
list2=[]
for i in range(1,n+1):
    if n%i==0:
        list1.append(i)
for j in range(1,k+1):
    if k%j==0:
        list2.append(j)

if n<k:
    list1.sort(reverse=True)
    for i in range(len(list1)):
        if list1[i] in list2:
            print(list1[i])
            break
if n>k:
    list2.sort(reverse=True)
    for j in range(len(list2)):
        if list2[j] in list1:
            print(list2[j])
            break
