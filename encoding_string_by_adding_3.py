text=input()
text=str(text)
new_text=[]
for i in range (len(text)):
    if text[i]=='x':
        new_text.append('a')
    elif text[i]=='X':
        new_text.append('A')
    elif text[i]=='y':
        new_text.append('b')
    elif text[i]=='Y':
        new_text.append('B')
    elif text[i]=='z':
        new_text.append('c')
    elif text[i]=='Z':
        new_text.append('C')
    else:
        new_text.append(chr(ord(text[i])+3))
strin="".join(new_text)
print(strin)
    

