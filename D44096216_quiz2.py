amount=input("Enter the shopping amount: ")
which=input("Enter the membership level(Regular or Gold): ")
a=float(amount)
if which=="Regular":
	if 1000<=a<2000:
		total=a*0.9
		print(which,"$",total)
	elif 2000<=a<3000:
		total=a*0.85
		print(which,"$",total)
	elif 3000<=a:
		total=a*0.8
		print(which,"$",total)
	else:
		total=a
		print(which,"$",total)
else:
 	if which=="Gold":
 		if 1000<=a<2000:
 			total=fa*0.85
 			print(which,"$",total)
 		elif 2000<=a<3000:
 			total=a*0.8
 			print(which,"$",total)
 		elif 3000<=a:
 			total=a*0.75
 			print(which,"$",total)
 		else:
 			total=a
 			print(which,"$",total)
 	else:
 		print("Invalid member level. Please enter \'Regular\' or \'Gold\' ")