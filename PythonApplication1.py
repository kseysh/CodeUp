height,width=map(int,input().split())
stickCount=int(input())
ldxy=[[0 for col in range(4)] for row in range(stickCount)]
for a in range(stickCount):
	ldxy[a]=list(map(int,input().split(' ')))
#d는 0이 가로

grid = [[0 for col in range(height)] for row in range(width)]

for count in range(stickCount):
	for col in range(width):
		for row in range(height):
			grid[ldxy[count][2]][ldxy[count][3]]=1
#			if ldxy[1][count] == 0:

#			else:
	

for col in range(stickCount):
	for row in range(4):
		print(ldxy[col][row],end=' ')
	print('\n')
# ldxy가 잘 작동하는지 확인용

for col in range(width):
	for row in range(height):
		print(grid[col][row],end=' ')
	print('\n')
#판 프린트용