N=input()
lis=input().split()
s='kabali'
s=list(s)
count=0
for i in range(len(lis)):
    tem=lis[i]
    if tem.count('k')==1:
        if tem.count('a')==2:
            if tem.count('b')==1:
                if tem.count('l')==1:
                    if tem.count('i')==1:
                        if len(tem)==len(s):
                            count=count+1

print(count)
