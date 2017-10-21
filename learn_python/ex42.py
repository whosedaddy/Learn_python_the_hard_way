##Animal is_a object (yes,sort of confusing) look at the extra credit
class Animal(object):
	pass
	
##Dog is_a Animal
class Dog(Animal):
	
	def __init__(self,name):
		##Dog has_a name
		self.name=name
		
##Cat is_a Animal
class Cat(Animal):
	
	def __init__(self,name):
		##Cat has_a name
		self.name=name
		
##Person is_a Animal
class Person(object):
	
	def __init__(self,name):
		##Person has_a name
		self.name=name
		
		##Person has_a pet of some kind
		self.pet=None
		
##Employee is_a Person
class Employee(Person):
	
	def __init__(self,name,salary):
		##has_a hmm what is this strange magic?
		super(Employee,self).__init__(name)
		##Emloyee has_a salary
		self.salary=salary
		
##Fish is_a object
class Fish(object):
	pass
	
##Salmon is_a Fish
class Salmon(Fish):
	pass
	
##Halibut is_a Fish
class Halibut(Fish):
	pass
	
	
##rover is_a Dog
rover=Dog("Rover")

##satan is_a Cat
satan=Cat("Satan")

##mary is_a Person
mary=Person("Mary")

##mary has_a pet
mary.pet=satan

##frank is_a employee
frank=Employee("Frank",120000)

##frank has_a pet
frank.pet=rover

##flipper is_a fish
flipper=Fish()

##crouse is_a samlon
crouse=Salmon()

##harry is_a halibut
harry=Halibut()

print "Frank's pet is:%s"%frank.pet.name