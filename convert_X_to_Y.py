s,t=input().split()
s=list(s)
t=list(t)
j=0
a=len(s)
b=len(t)
count=min(a,b)
max_len=max(a,b)

for i in range (count):
    if s[i]==t[i]:
        max_len=max_len-1
        continue
    else:
        j=j+1
        max_len=max_len-1

j=j+max_len
print (j)
