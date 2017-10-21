def re(n,f,t,s):
	if n==1:
		print "From %s to %s."%(f,t)
	else:
		re(n-1,f,s,t)
		re(1,f,t,s)
		re(n-1,s,t,f)

re(10,'f','t','s')