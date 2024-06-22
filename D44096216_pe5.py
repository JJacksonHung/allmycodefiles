#輸入grid的邊長
num=int(input("Enter the size of the grid:"))
grid=[]
i=0
#用-的樣式印出grid
while i < num*num:
	grid.append("-")
	i+=1
grid_str=""
i=0
#將grid轉成正方形
while i < num*num:
	row=grid[i:i+3]
	grid_str+="".join(row)+"\n"
	i+=num

print(grid_str)

#輸入要改變的位置和圖示
while True:
	edit=input("Enter the cell coordinate to edit: ")
	if edit=="done":
		break
	cell=input("Enter the new value for the cell:")
	#提取要改變位置的數字
	number=int(edit[0])*num+int(edit[2])
	#用新的圖示取代-
	grid[number]=grid[number].replace("-",cell)
	i=0
	#印出新的正方形
	new_grid_str=""
	while i < num*num:
		row=grid[i:i+3]
		new_grid_str+="".join(row)+"\n"
		i+=num
	print(new_grid_str)
