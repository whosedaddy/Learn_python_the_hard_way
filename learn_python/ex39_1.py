states={
	'Beijing':'BJ',
	'Shanghai':'SH',
	'Guangdong':'GD',
	'Zhejiang':'ZJ',
	'Chongqing':'CQ',
	'Hubei':'HB'
	}
	
cities={
	'BJ':'Bei Jing',
	'SH':'Shang Hai',
	'GD':'Guang dong',
	'ZJ':'Hang zhou',
	}
	
cities['CQ']='Chong qing'
cities['HB']='Wu han'

print '-'*10
print "BJ State has:",cities['BJ']
print "SH State has:",cities['SH']

print '-'*10
print "Chongqing's abbreviation is:",states['Chongqing']
print "Hubei's abbreviation is:",states['Hubei']

print '-'*10
print "Chongqing has:",cities[states['Chongqing']]
print "Hubei has:",cities[states['Hubei']]

print '-'*10
for state,abbre in states.items():
	print "%s is abbreviated %s"%(state,abbre)
	
print '-'*10
for abbre,city in cities.items():
	print "%s has the city %s"%(abbre,city)
	
print '-'*10
for state,abbre in states.items():
	print "%s state is abbreviated %s and has city %s"%(
		state,abbre,cities[abbre])
	
state=states.get('Sichuan')

if not state:
	print "Sorry,no Sichuan."
	
city=cities.get('SC','Does not exist')
print "The city for the state 'SC' is:%s"%city