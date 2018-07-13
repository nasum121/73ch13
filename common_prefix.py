n=int(input())
string1=input()
string2=input()
s1=list(string1)
s2=list(string2)
new_word=[]
a=len(s1)
b=len(s2)
if a>b:
    count=b
else:
    count=a
for i in range(count):
    if s1[i]==s2[i]:
        new_word.append(s1[i])
new="".join(new_word)
print(new)
