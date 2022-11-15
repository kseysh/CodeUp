inputnum=int(inpt())
for a in range(1,inputnu+1):
	a=str(a)
	if a.find('3')==-1 and a.find('6')==-1 and a.find('9')==-1:
		a=int(a)
		print(a,end=' ')
	else :	
		print('X',end=' ')
