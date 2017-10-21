class Person(object):#define a Person class which have four attributes
	
	def __init__(self):
		self.hpa=100
		self.hp=100
		self.mpa=100
		selg.mp=100
		self.ex=0
		self.lv=1
		
		
class Hero(Person):#dedine a Hero who has a power buff skill
	
	def __init__(self):
		self.attack=80
		self.defense=30
		
	def powerp(self):
		if self.mp-33>=0:
			self.mp-=33
			self.attack+=50
		else print "Your MP is inadequate."
		
	def powerl(self):
		self.attack-=50

	
class Clergy(Person):#define a Clergy who can help other add HP or MP

	def __init__(self):
		self.attack=60
		self.defense=40
		
	def hpp(self,who):
		if self.mp-33>=0:
			self.mp-=33
			who.hp+=33
			if who.hp>who.hpa:
				who.hp=who.hpa
				print "Your HP is full."
		else print "Your MP is inadequate."
		
	def mpp(self,who):
		who.mp+=33
		if who.mp>who.mpa:
			who.mp=who.mpa
			print "Your MP is full."
		
		
class Warrior(Person):#define a Warrior who has a powerful buff

	def __init__(self):
		self.attack=90
		self.defense=50
	
	def buffall(self):
		if self.mp-33>=0:
			self.mp-=33
			self.attack+=20
			self.defense+=10
			if self.hp+20<=self.hpa:
				self.hp+=20
			else self.hp=self.hpa
			
class Theft(Person):#define a Theft who can steal money from enemy
	
	def __init__(self):
		self.attack=70
		self.defense=45		
		
	def steal(self,person):
		if self.mp-33>=0:
			self.mp-=33
			self.moneys+=person.money*0.5
			
class Supplies(object):#define a repository to store your supplies
	
	def __init__(self):
		self.hpotion=5
		self.mpotion=5
		self.money=0
		
	def use(self,person):
		m=raw_input("Please choose to use hpotion or mpotion.")
		if m="hoption" and self.hpotion>0:
			self.hpotion-=1
			person.hp+=person.hpa*0.7
			if person.hp>=person.hpa:
				person.hp=person.hpa
				print "Your HP is full."		
		elif m="mpotion" and self.mpotion>0:
			self.mpotion-=1
			person.mp+=person.mpa*0.7
			if person.mp>=person.mpa:
				person.mp=person.mpa
				print "Your HP is full."	
		elif m="hoption" and self.hpotion<=0:
			print "You have no hpotion."
		elif m="moption" and self.mpotion<=0:
			print "You have no mpotion."
		else "Please input again."
		
	def getting(self,aperson,bperson):
		self.hpotion+=aperson.hopotion
		self.mpotion+=aperson.mpotion
		self.money+=bperson.moneys#Beware!!!
		
class Solider(Person):
	
	def __int__