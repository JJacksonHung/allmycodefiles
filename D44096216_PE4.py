s=input("Enter a sequence of integers separated by whitespace:")
#消除空格
s=s.split(" ")
i=0
v=[]
#一個一個拿出來
while i < len(s):
	#若i==0將所對應到的數字放到新串列v裡
	if i==0:
		v+=s[i]
		i=i+1
	#數字跟串列v的最後一個數比大小
	elif v[-1]<s[i]:
		v+=s[i]
		i=i+1
    #數字若是比串列v的最後一數字小且下一數字大於現在數字則清空目前的v串列
    #將數字放到新串列v裡
	elif v[-1]>s[i] and int(s[i+1])>int(s[i]):
		v=[]
		v+=s[i]
		i=i+1
		
print("Length:",len(v))
print("LICS:",v)
