from sys import exit

def apple_room():
	while 1:
		print "This is the apple_room."
		print "There are three apples on the table."
		print "You should choose one(1,2 or 3) and eat it."
		choice=raw_input('>')
	
		if '1' in choice:
			print "It's poisonous apple."
			dead("There is something weird.")
		elif '2' in choice:
			print "It's poisonous apple."
			dead("There is something weird.")
		elif '3' in choice:
			print "It's poisonous apple."
			dead("There is something weird.")
		elif 'taunt' in choice:
			print "You are a wise guy!The devil is feeble and you get the real apple."
			print "Congratulations!"
			exit(0)
		else:
			print "You should think twice.There is something weird."
		
def angel_room():
	while 1:
		print "There are two guy in front of your face."
		print "One is a angel,and another is devil."
		print "You should choose one to follow."
		choice=raw_input('>')
	
		if 'angel' in choice:
			print "The angel guide you to the paradise."
			dead("The paradise is beautiful.")
		elif 'devil' in choice:
			print "The devil lead you to the way to the apple,but you should be cautious."
			print "It might be a trick."
			apple_room()
		else:
			print "You should choose one and follow the guy."
		
def first_room():
	print "Your target is to find the real apple.Just be careful!"
	print "There are two doors in front of you."
	print "You shoule choose the left one or the right one."
	choice=raw_input('>')
	
	if 'right' in choice:
		angel_room()
	elif 'left'in choice:
		print "You fall off a cliff."
		dead("Good luck.")
	else:
		print "You are wrong."
		dead("Just choose the right way.")
		
def dead(string):
	print string,"Good job!"
	exit(0)
	
first_room()