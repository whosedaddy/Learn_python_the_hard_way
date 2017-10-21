def add(a,b):
	print "ADDING %d+%d"%(a,b)
	return a+b
	
def subtract(a,b):
	print "SUBTREACTING %d-%d"%(a,b)
	return a-b
	
def multiply(a,b):
	print "MULTIPLYING %d*%d"%(a,b)
	return a*b
	
def divide(a,b):
	print "DIVIDING %d/%d"%(a,b)
	return a/b
	
	
print "Let's do some math with just functions!"

age=add(30,5)
height=subtract(78,4)
weight=multiply(90,2)
iq=divide(1000,2)

print "Age:%d,Height:%d,Weight:%d,IQ:%d"%(age,height,weight,iq)

# A puzzle for the extra credit,type it in anyway.
print "Here is a puzzle."

what=add(age,subtract(height,multiply(weight,divide(iq,3))))

print "That's becomes:",what,"Can you do it by hand?"

stuff=divide(add(10,multiply(subtract(8,20),10)),10)

print "%d"%stuff