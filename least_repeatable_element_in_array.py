N=int(input())
array=input().split()
for i in range(N):
    if array.count(array[i])==1:
        print(array[i])
