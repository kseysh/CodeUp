mazebox=[[0 for col in range(10)] for row in range(10)]

for a in range(10):
	inputval=list(map(int,input().split()))
	mazebox[a]=inputval
		
a=1
b=1
while True:
	if mazebox[a][b]==0:
		mazebox[a][b]=9
		b+=1
	elif mazebox[a][b]==1:
		a+=1
		b-=1
	elif mazebox[a][b]==2:
		mazebox[a][b]=9
		break
	if a==8 and b==9:
		break


for a in range(10):
	for b in range(10):
		print(mazebox[a][b],end=' ')
	print()
#mazebox print