height,width=map(int,input().split())
stickCount=int(input())
ldxy=[[0 for col in range(4)] for row in range(stickCount)]
for a in range(stickCount):
	ldxy[a]=list(map(int,input().split(' ')))
#d는 0이 가로

grid = [[0 for col in range(height)] for row in range(width)]

for count in range(stickCount):
	if ldxy[count][1] == 0:
		for i in range(ldxy[count][3],ldxy[count][3]+ldxy[count][0]):
			grid[i-1][ldxy[count][2]-1]=1
	else:
		for j in range(ldxy[count][2],ldxy[count][2]+ldxy[count][0]):
			grid[ldxy[count][3]-1][j-1]=1
# 막대기 놓는 식

for row in range(height):
	for col in range(width):
		print(grid[col][row],end=' ')
	print()
#판 프린트용