s=input()
s=list(s)
new=[]
vowels='aeiouAEIOU'
vowels=list(vowels)
for i in range(len(s)):
    if s[i] not in vowels:
        new.append(s[i])
               
c="".join(new)
print(c[::-1])
