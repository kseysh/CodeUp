
i,j=0,0
arr = [[0 for col in range(19)] for row in range(19)]
while i<19:
	temp=list(map(int,input().split()))
	while j<19:
		arr[i][j]=temp[j]
		j+=1
	i+=1
	j=0
	temp.clear()
i,j=0,0

num=int(input())
inputnumarr = [[0 for col in range(2)] for row in range(num)]

for k in range(num):
	imsilist=list(map(int,input().split()))
	inputnumarr[k][0]=imsilist[0]-1
	inputnumarr[k][1]=imsilist[1]-1


i=0
while i<19:
	j=0
	while j<19:
		for k in range(num):
			if inputnumarr[k][0]==j:
				if arr[j][i]==1:
					arr[j][i]=0
				elif arr[j][i]==0 :
					arr[j][i]=1	
		for p in range(num):
			if inputnumarr[p][1]==i:
				if arr[j][i]==1:
					arr[j][i]=0
				elif arr[j][i]==0:
					arr[j][i]=1
		j+=1

		
	i+=1

i,j=0,0
while i<19:
	while j<19:
		print(arr[i][j], end=' ')
		j+=1
	i+=1
	j=0
	print()
