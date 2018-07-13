n,s=input().split()
n=int(n)
s=list(s)
new=[]
vowels='aeiouAEIOU'
vowels=list(vowels)
for i in range(n):
    if s[i] not in vowels:
        new.append(s[i])
               
c="".join(new)
print(c[::-1])
