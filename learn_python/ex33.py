def range_numbers(number,incre):
	a=[]
	i=0
	while i<number:
		print "At the top i is %d"%i
		a.append(i)
		
		i=i+incre
		print "number now:",a
		print "At the bottom i is %d"%i
	return a

i=0
numbers = []
i=6
numbers.extend(range_numbers(i,2))

#while i<6:
#	print "At the top i is %d"%i
#	numbers.append(i)
#	
#	i=i+1
#	print "Number now:",numbers
#	print "At the bottom i is %d"%i
	
print "The numbers:"

for num in numbers:
	print num,