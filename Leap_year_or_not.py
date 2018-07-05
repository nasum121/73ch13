nm=int(input())
if num%100==0:
	if num%400==0:
		print ("yes")
	else:
		print ("no")
elif num%4==0:
	print ("yes")
else:
	print ("no")
