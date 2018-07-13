n=int(input())
if n==2:
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
if n==3:
    string1=input()
    string2=input()
    string3=input()
    s1=list(string1)
    s2=list(string2)
    s3=list(string3)
    new_word=[]
    final=[]
    a=len(s1)
    b=len(s2)
    c=len(s3)
    count=min(a,b,c)
    for i in range(count):
        if s1[i]==s2[i]==s3[i]:
            new_word.append(s1[i])

        
    final="".join(new_word)
    print(final)
if n==4:
    string1=input()
    string2=input()
    string3=input()
    string4=input()
    s1=list(string1)
    s2=list(string2)
    s3=list(string3)
    s4=list(string4)
    new_word=[]
    
    a=len(s1)
    b=len(s2)
    c=len(s3)
    d=len(s3)
    count=min(a,b,c,d)
    for i in range(count):
        if s1[i]==s2[i]==s3[i]==s4[i]:
            new_word.append(s1[i])
    final="".join(new_word)
    print(final)
if n==5:
    string1=input()
    string2=input()
    string3=input()
    string4=input()
    string5=input()
    s1=list(string1)
    s2=list(string2)
    s3=list(string3)
    s4=list(string4)
    s5=list(string5)
    new_word=[]
    
    a=len(s1)
    b=len(s2)
    c=len(s3)
    d=len(s3)
    e=len(s4)
    count=min(a,b,c,d,e)
    for i in range(count):
        if s1[i]==s2[i]==s3[i]==s4[i]==s5[i]:
            new_word.append(s[i])
    final="".join(new_word)
    print(final)
if n==6:
    string1=input()
    string2=input()
    string3=input()
    string4=input()
    string5=input()
    string6=input()
    s1=list(string1)
    s2=list(string2)
    s3=list(string3)
    s4=list(string4)
    s5=list(string5)
    s6=list(string6)
    new_word=[]
    
    a=len(s1)
    b=len(s2)
    c=len(s3)
    d=len(s3)
    e=len(s4)
    f=len(s5)
    
    count=min(a,b,c,d,e,f)
    for i in range(count):
        if s1[i]==s2[i]==s3[i]==s4[i]==s5[i]==s5[i]:
            new_word.append(s1[i])
    final="".join(new_word)
    print(final)
