countnum=int(input())
randnumarr=list(map(int,input().split()))
studentnumarr=list(range(23))

for a in range(23):
	studentnumarr[a]=0

for a in range(countnum):
	studentnumarr[randnumarr[a]-1]+=1

for a in range(23):
	print(studentnumarr[a], end=' ')