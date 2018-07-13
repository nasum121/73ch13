string=input()
string=list(string)
max=1

for i in range(len(string)):
    count=0
    for j in range(len(string)):
                   
                   if string[i]==string[j]:
                       count=count+1
                   if (count>max):
                       count=max
                       key=string[i]
print(key)
                   
                   
