num=input("enter the number to be checked \n")
if num.isdigit():
	num=int(num)
	if num%2==0:
		print ("Even")
	else:
		print ("Odd")
else:
	print ("Invalid")
