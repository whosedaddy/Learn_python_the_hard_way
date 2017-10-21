a='1,2,3,4'
b='abcd'
p=[]
for i in a,b:
	m=i[:]
	p.append(m)
	print i,m,p
c,d=p
print c,d
c,d=d,c
print d