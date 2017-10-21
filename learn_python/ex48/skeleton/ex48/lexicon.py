import string
def convert_number(s):
	try:
		return string.atoi(s)
	except ValueError:
		return None
		
		
def scan(string):
	directions=['north','south','east','west','down','up','left','right','back']
	verbs=['go','stop','kill','eat']
	stops=['the','in','of','from','at','it']
	nouns=['door','bear','princess','cabinet']
	words=string.split()
	sentence=[]
	#find what type the words' elements is
	for i in range(0,len(words)):
		if words[i] in directions:
			first_word=('direction',words[i])
			sentence.append(first_word)
		elif words[i] in verbs:
			second_word=('verb',words[i])
			sentence.append(second_word)
		elif words[i] in stops:
			third_word=('stop',words[i])
			sentence.append(third_word)
		elif words[i] in nouns:
			fourth_word=('noun',words[i])
			sentence.append(fourth_word)
		else:
			if convert_number(words[i]) != None:
				fifth_word=('number',convert_number(words[i]))
				sentence.append(fifth_word)
			else:
				fifth_word=('error',words[i])
				sentence.append(fifth_word)
	
	return sentence