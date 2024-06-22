import random
a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
"q","r","s","t","u","v","w","x","y","z"]
random.shuffle(a) #隨機抽一個字母
deck=a[0]
num=0
while True:
	guess=input("Guess the lowercase alphabet: ")
	if guess!=deck:
		if guess<deck:
			print("The alphabet you are looking for is alphabetically higher.")
			num+=1
		if guess>deck:
			print("The alphabet you are looking for is alphabetically lower.")
			num+=1
		if guess==deck.upper() :
			print("Please enter a lowercase alphabet")
			num+=1
	if guess==deck:
		num+=1
		print("Congratulations! You guessed the alphabet","\"",deck,"\"","in",num,"tries.")
		break

