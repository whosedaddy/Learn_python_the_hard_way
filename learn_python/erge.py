data=open('erge.txt','w')

i=2
j=0
m=2
n=4

while(i<31):
	f='group sec%d range y %d %d group insiderocks\n'%(i,m,n)
	s='group sec%d range y %d %d group concretliners\n'%(i,m,n)
	t='group sec%d range y %d %d group insiderockx\n'%(i,j,m)
	th='group sec%d range y %d %d group concretlinerx\n'%(i,j,m)
	data.write(f)
	data.write(s)
	data.write(t)
	data.write(th)
	i=i+1
	j+=2
	m+=2
	n+=2