#印出歡迎詞
print("Welcome to the simple calculator program!")
#讓程式不斷被執行
while True:
	#輸入數值和要怎麼運算
	first_number=float(input("Enter the first number: "))
	second_number=float(input("Enter the second number: "))
	operation=input("Select an arithmetic operation(+,-,*,/): ")
	#加入條件：除法過程中若分母為零則顯示錯誤，並重新執行程式
	if operation=="/" and second_number==0:
		print("Error: Division by zero!")
		continue
	#加入加法的運算過程
	elif operation=="+":
		cal=first_number+second_number
		print("Result:",float(cal))
		#詢問要不要再運算其他的
		ask=input("Do you want to perform another calculation>(yes or no):")
		if ask=="yes":
			continue
		else:
			print("Goodbye!")
			break
	#加入減法的運算過程
	elif operation=="-":
		cal=first_number - second_number
		print("Result:",float(cal))
		#詢問要不要再運算其他的
		ask=input("Do you want to perform another calculation>(yes or no):")
		if ask=="yes":
			continue
		else:
			print("Goodbye!")
			break
	#加入乘法的運算過程
	elif operation=="*":
		cal=first_number * second_number
		print("Result:",float(cal))
		#詢問要不要再運算其他的
		ask=input("Do you want to perform another calculation>(yes or no):")
		if ask=="yes":
			continue
		else:
			print("Goodbye!")
			break
	#加入除法的運算過程
	elif operation=="/":
		cal=first_number / second_number
		print("Result:",float(cal))
		#詢問要不要再運算其他的
		ask=input("Do you want to perform another calculation>(yes or no):")
		if ask=="yes":
			continue
		else:
			print("Goodbye!")
			break
	else:
		continue



