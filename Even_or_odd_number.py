a=input("enter the number to be checked \n")
if a.isdigit():
	a=int(a)
	if a%2==0:
		print ("Even")
	else:
		print ("Odd")
else:
	print ("Invalid")
