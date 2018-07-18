string=input()
numericals=['1','2','3','4','5','6','7','8','9','0',]
count=0
for i in range(len(string)):
    if string[i] in numericals:
        count=count+1
        if count==len(string): 
            print("yes")
            break
    else:
        print("no")
        break
