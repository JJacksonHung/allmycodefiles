#從9X9開始
i,j=9,9
#每一組的j都是相同的，因此先給定j，在此j的底下進行i的運算
while j>0:
	while i>0:
		print(i,"x",j,"=",i*j,end="\t")
		print(i,"x",(j-1),"=",i*(j-1),end="\t")
		print(i,"x",(j-2),"=",i*(j-2),end="\n")
		#每ㄧ列的i相差1
		i=i-1
	#印出空白列
	print()
	#上一大列的j與下一大列的j相差3
	j=j-3
	#重設i讓每一組的i都是從9開始遞減
	i=9
