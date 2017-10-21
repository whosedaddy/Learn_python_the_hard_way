def number_one_function(first,second,third):
	print "The first argument is %s."%first
	print "The second argument is %s."%second
	print "The third argument is %s."%third

print "This is the first way to run the function."
number_one_function(10,11,12)

print "This is the second way to run the function."
number_one_function("a","b","c")

print "This is the third way to run the function."
number_one_function(1+2,2+3,3+4)

print "This is the fourth way to run the function."
number_one_function("a"+"b","c"+"d","e"+"f")

print "This is the fifth way to run the function."
I="a"
II="b"
III="c"
number_one_function(I,II,III)

print "This is the sixth way to call the function."
number_one_function(I+I,II+II,III+III)

print "This is the seventh way to call the function."
number_one_function(I+'b',II+"a",III+"c")

print "This is the eighth way to use the function."
number_one_function(I+'a',"abc",'c'+'b'+'a')

print "This is the ninth way to call the function."
IV=raw_input(">")
V=raw_input(">")
number_one_function(IV,V,I)

print "This is the tenth way to run the function."
number_one_function(raw_input(">"),raw_input(">"),raw_input(">"))