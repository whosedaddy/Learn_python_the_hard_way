def test(num,str,list,dic):
	num=num+1
	str=str+"NEW"
	list[0]="You"
	dic['a']=5
	print num
	print str
	print list
	print dic
	
num=1
str="OLD"
list=["I","like","python"]
dic={"a":1,"b":2}
test(num,str,list,dic)
print num#no change
print str#no change
print list#changed
print dic#changed