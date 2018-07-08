from random import randint
ran=randint(1000,9999)
print (ran)

digits=[int(x) for x in str(ran)]

print(digits)





user_num=input("enter the number")
user_digits=[int(y) for y in str(user_num)]
print(user_num)


if ran[0]==user_num[0]:
        print(ran[i],"is bull")
